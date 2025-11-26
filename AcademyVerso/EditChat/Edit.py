"""Edit utilities for batch and single-file edits using the Refactor module.

Funciones principales:
- `load_default_prompt()`: carga el prompt por defecto desde `Refactor/example_refactor_prompt.md`.
- `edit_code(code, prompt=None, backend='auto')`: usa `Refactor.refactor_code`.
- `edit_file(path, prompt=None, backup=True, backend='auto')`: edita un archivo en disco (con backup opcional).
- `batch_edit(folder, pattern='**/*.py', prompt=None, dry_run=True, backend='auto')`: aplica el prompt por defecto a todos los archivos que coincidan.
- `preview_edit(path, prompt=None, backend='auto')`: devuelve el resultado sin escribir en disco.

Este archivo está pensado para ser no interactivo: usa el prompt por defecto si no se provee.
"""
import os
from pathlib import Path
from typing import Optional, List

from AcademyVerso.Refactor.refactor import refactor_code


DEFAULT_PROMPT_PATH = Path(__file__).resolve().parents[1] / "Refactor" / "example_refactor_prompt.md"


def load_default_prompt() -> str:
    if DEFAULT_PROMPT_PATH.exists():
        return DEFAULT_PROMPT_PATH.read_text(encoding="utf-8")
    return "Mejora nombres y formato, añade docstrings"


def edit_code(code: str, prompt: Optional[str] = None, backend: str = "auto") -> str:
    if not prompt:
        prompt = load_default_prompt()
    return refactor_code(prompt, code, backend=backend)


def preview_edit(path: str, prompt: Optional[str] = None, backend: str = "auto") -> str:
    code = Path(path).read_text(encoding="utf-8")
    return edit_code(code, prompt=prompt, backend=backend)


def edit_file(path: str, prompt: Optional[str] = None, backup: bool = True, backend: str = "auto") -> str:
    p = Path(path)
    original = p.read_text(encoding="utf-8")
    edited = edit_code(original, prompt=prompt, backend=backend)
    if edited != original:
        if backup:
            bak = p.with_suffix(p.suffix + ".bak")
            bak.write_text(original, encoding="utf-8")
        p.write_text(edited, encoding="utf-8")
    return edited


def batch_edit(folder: str, pattern: str = "**/*.py", prompt: Optional[str] = None, dry_run: bool = True, backend: str = "auto") -> List[str]:
    root = Path(folder)
    files = list(root.glob(pattern))
    changed = []
    for f in files:
        original = f.read_text(encoding="utf-8")
        edited = edit_code(original, prompt=prompt, backend=backend)
        if edited != original:
            changed.append(str(f))
            if not dry_run:
                bak = f.with_suffix(f.suffix + ".bak")
                bak.write_text(original, encoding="utf-8")
                f.write_text(edited, encoding="utf-8")
    return changed


if __name__ == "__main__":
    # Ejemplo de uso no interactivo
    project_root = Path(__file__).resolve().parents[1]
    demo_file = project_root / "examples" / "ask_demo.py"
    if demo_file.exists():
        print("Preview edit for:", demo_file)
        print(preview_edit(str(demo_file)))
    else:
        print("Archivo demo no encontrado. Usa `edit_file` o `batch_edit` desde tu código.")
