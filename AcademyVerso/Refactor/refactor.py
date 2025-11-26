"""Utilities to refactor code using a prompt.

Provides `refactor_code(prompt, code, backend='auto')`.

Backends:
- 'local': a simple heuristic-based refactor (uses AST for Python)
- 'openai' or 'llm': sends prompt+code to an LLM via OpenAI (if API key set)
- 'auto': picks 'openai' if `OPENAI_API_KEY` env var exists, otherwise 'local'

This file intentionally keeps the LLM integration optional and minimal.
"""
from typing import Optional
import os
import ast

try:
    import astor
except Exception:
    astor = None


def _local_refactor(prompt: str, code: str) -> str:
    """A naive local refactor: formats code, renames short variable names, and
    applies a couple of safe AST-based transforms.

    This is intentionally conservative — it's a placeholder that you can
    extend with more sophisticated rules.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return code

    class RenameShortVars(ast.NodeTransformer):
        def __init__(self):
            self.map = {}
            self.counter = 0

        def _new_name(self, old):
            if old in self.map:
                return self.map[old]
            self.counter += 1
            new = f"var_{self.counter}"
            self.map[old] = new
            return new

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store) and len(node.id) <= 2:
                node.id = self._new_name(node.id)
            return node

    tree = RenameShortVars().visit(tree)
    ast.fix_missing_locations(tree)

    try:
        if astor:
            refactored = astor.to_source(tree)
        else:
            # Fallback to ast.unparse (Python 3.9+)
            refactored = ast.unparse(tree)
    except Exception:
        refactored = code

    # Minimal formatting: strip trailing spaces
    refactored = "\n".join(line.rstrip() for line in refactored.splitlines())
    return refactored


def _openai_refactor(prompt: str, code: str, api_key: Optional[str]) -> str:
    """Call OpenAI's API to refactor. This is a minimal implementation that
    expects the user to set `OPENAI_API_KEY` in the environment. If the key is
    not available or requests fails, falls back to returning the original code.

    Note: we do not add `openai` to requirements here to keep this repo
    dependency-free. If you want LLM support, install `openai` and set the
    API key.
    """
    if not api_key:
        return code

    try:
        import openai
    except Exception:
        return code

    openai.api_key = api_key
    system = "You are a helpful code refactoring assistant. Return only the refactored code."
    user_message = f"""Prompt:
{prompt}

Code:
```
{code}
```

Refactor the code according to the prompt. Return only the refactored code."""

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user_message}],
            temperature=0.2,
            max_tokens=2000,
        )
        text = resp.choices[0].message.content.strip()
        return text
    except Exception:
        return code


def refactor_code(prompt: str, code: str, backend: str = "auto") -> str:
    """Refactor `code` according to `prompt` using the chosen backend.

    backend: 'auto'|'local'|'openai'|'llm'
    """
    if backend == "auto":
        if os.environ.get("OPENAI_API_KEY"):
            backend = "openai"
        else:
            backend = "local"

    if backend in ("openai", "llm"):
        api_key = os.environ.get("OPENAI_API_KEY")
        return _openai_refactor(prompt, code, api_key)

    return _local_refactor(prompt, code)


if __name__ == "__main__":
    sample = """
def sum(a,b):
 return a+b
"""
    prompt = "Mejora nombres y formato"
    print(refactor_code(prompt, sample, backend="local"))
