"""Demo runner minimal para las 13 demos.

Notas:
- Este script es un conjunto de funciones que simulan llamadas a APIs de modelo.
- No incluye llamadas reales a APIs externas por seguridad (evita exponer claves).
- Para usar con una API real, implementa `call_model(prompt, **kwargs)`.
"""
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PROMPTS = BASE / 'prompts' / 'demo_prompts.md'


def load_prompts():
    with open(PROMPTS, 'r', encoding='utf-8') as f:
        return f.read()


def call_model(prompt, mode='simulate', **kwargs):
    """Simula o envía un prompt a un modelo.

    mode: 'simulate' retorna una respuesta ficticia.
    """
    if mode == 'simulate':
        return {'response': f"[SIMULATED RESPONSE] Para prompt: {prompt[:80]}..."}
    # Aquí se implementaría la llamada real a la API, p.ej. usando requests
    raise NotImplementedError('Implementa call_model con tu cliente de API')


def demo_premium_request():
    p = load_prompts()
    prompt = 'premium_request: ' + ' '.join(p.splitlines()[:2])
    res = call_model(prompt)
    print('--- Premium Request ---')
    print(json.dumps(res, indent=2, ensure_ascii=False))


def demo_choose_model():
    p = load_prompts()
    prompt = 'choose_model_classification: ' + ' '.join(p.splitlines()[2:4])
    res = call_model(prompt)
    print('--- Choosing Model ---')
    print(res['response'])


def demo_chat_modes():
    p = load_prompts()
    prompt = 'chat_mode_system: ' + ' '.join(p.splitlines()[6:8])
    res = call_model(prompt)
    print('--- Chat Modes ---')
    print(res['response'])


def demo_ask():
    p = load_prompts()
    prompt = 'ask_rag: ' + 'Ejemplo: ¿Cuál es la política de privacidad?'
    res = call_model(prompt)
    print('--- Ask (RAG) ---')
    print(res['response'])


def demo_edits():
    p = load_prompts()
    prompt = 'edits_text: ' + 'Por favor mejora: "Este texto es un ejemplo largo que necesita pulir."'
    res = call_model(prompt)
    print('--- Edits ---')
    print(res['response'])


def demo_agent():
    prompt = 'agent_api: Llamar a API pública y extraer título y fecha.'
    res = call_model(prompt)
    print('--- Agent ---')
    print(res['response'])


def demo_plan_insiders():
    prompt = 'plan_mvp: Crear plan para MVP en 6 semanas.'
    res = call_model(prompt)
    print('--- Plan (Insiders) ---')
    print(res['response'])


def demo_next_edit_suggestions():
    prompt = 'next_edit_suggestion: Mejorar documentación de README.'
    res = call_model(prompt)
    print('--- Next Edit Suggestions ---')
    print(res['response'])


def demo_code_review():
    prompt = 'code_review: def foo(x): return x/0'
    res = call_model(prompt)
    print('--- Code Review ---')
    print(res['response'])


def demo_prompt_files():
    prompt = 'prompt_file_example: Crear endpoint POST /items'
    res = call_model(prompt)
    print('--- Prompt Files ---')
    print(res['response'])


def demo_custom_chat_modes():
    prompt = 'custom_chat_mode_support: Iniciar modo Soporte Técnico'
    res = call_model(prompt)
    print('--- Custom Chat Modes ---')
    print(res['response'])


def demo_copilot_github():
    prompt = 'copilot_example: Implementa factorial en Python'
    res = call_model(prompt)
    print('--- Copilot en GitHub ---')
    print(res['response'])


def demo_mcp():
    prompt = 'mcp_tool_example: Registrar tool GET /status'
    res = call_model(prompt)
    print('--- MCP ---')
    print(res['response'])


def main():
    demo_premium_request()
    demo_choose_model()
    demo_chat_modes()
    demo_ask()
    demo_edits()
    demo_agent()
    demo_plan_insiders()
    demo_next_edit_suggestions()
    demo_code_review()
    demo_prompt_files()
    demo_custom_chat_modes()
    demo_copilot_github()
    demo_mcp()


if __name__ == '__main__':
    main()
