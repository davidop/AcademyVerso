"""Ask over code demo placed in AcademyVerso/AskChat.

This script loads the local prompt and target file under AcademyVerso.
"""
from pathlib import Path
import json
import os
import traceback

BASE = Path(__file__).resolve().parent
PROMPT_TEMPLATE = (BASE / 'ask_over_code_prompt.md').read_text(encoding='utf-8')
TARGET = BASE.parent / 'CodeReview' / 'AcademyVerso_buggy.py'


def simulate_ask(code, question):
    if 'eval' in question.lower():
        return {
            'summary': 'El archivo contiene utilidades y funciones con varios problemas de seguridad y robustez.',
            'answer': 'La función `dangerous_eval` usa eval() sobre input externo, lo que permite ejecución arbitraria de código.',
            'lines': [20, 24]
        }
    if 'sql' in question.lower() or 'injection' in question.lower():
        return {
            'summary': 'El archivo guarda entradas de usuario en una base de datos usando concatenación de strings.',
            'answer': 'La función `save_user_input` construye una query concatenando el nombre del usuario, lo que es vulnerable a SQL injection. Usa parámetros.',
            'lines': [40, 50]
        }
    return {
        'summary': 'El archivo contiene funciones para procesar valores, manejar config y ejecutar entradas del usuario.',
        'answer': 'No estoy seguro; ¿puedes preguntar sobre una parte concreta (p. ej. uso de eval o ejecución de comandos)?',
        'lines': []
    }


def call_remote_llm(prompt_text):
    """Call a generic HTTP LLM endpoint configured with env vars.

    Expected env vars (optional):
    - LLM_API_URL : full URL to POST the prompt to
    - LLM_API_KEY : bearer token (optional)
    - LLM_MODEL   : model identifier (optional; sent in JSON)

    The function attempts a best-effort POST with JSON {"model":..., "prompt":...}
    and accepts several common JSON response shapes. On any error it raises.
    """
    try:
        import requests
    except Exception:
        raise RuntimeError('`requests` library is required for remote LLM calls')

    url = os.environ.get('LLM_API_URL')
    if not url:
        raise ValueError('LLM_API_URL is not set')

    payload = {
        'prompt': prompt_text
    }
    model = os.environ.get('LLM_MODEL')
    if model:
        payload['model'] = model

    headers = {'Content-Type': 'application/json'}
    api_key = os.environ.get('LLM_API_KEY')
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'

    resp = requests.post(url, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()

    # Try to parse common response shapes
    try:
        data = resp.json()
    except ValueError:
        # not json, return raw text
        return {'summary': 'Respuesta remota (texto)', 'answer': resp.text, 'lines': []}

    # OpenAI-like: choices[0].message.content
    if isinstance(data, dict):
        if 'choices' in data and isinstance(data['choices'], list) and data['choices']:
            first = data['choices'][0]
            if isinstance(first, dict):
                # Chat-style
                msg = first.get('message') or first.get('text') or first.get('content')
                if isinstance(msg, dict):
                    text = msg.get('content')
                else:
                    text = msg
                return {'summary': 'Respuesta remota', 'answer': text or json.dumps(first, ensure_ascii=False), 'lines': []}

        # simple shaped responses
        for key in ('answer', 'text', 'result', 'output'):
            if key in data:
                return {'summary': 'Respuesta remota', 'answer': data[key], 'lines': []}

    # fallback: stringify
    return {'summary': 'Respuesta remota (sin formato conocido)', 'answer': json.dumps(data, ensure_ascii=False), 'lines': []}


def main():
    code = TARGET.read_text(encoding='utf-8')
    question = input('Pregunta sobre el código: ').strip()
    prompt = PROMPT_TEMPLATE.replace('{{CODE}}', code).replace('{{QUESTION}}', question)
    print('--- Prompt enviado ---\n')
    print(prompt[:1000])
    print('\n--- Respuesta simulada ---\n')
    # If an LLM endpoint is configured, try to call it. Otherwise use simulation.
    try:
        if os.environ.get('LLM_API_URL'):
            try:
                llm_resp = call_remote_llm(prompt)
                print(json.dumps(llm_resp, indent=2, ensure_ascii=False))
                return
            except Exception as e:
                print('Error llamando al LLM remoto:', str(e))
                traceback.print_exc()
                print('\nCayendo a respuesta simulada...')

    except Exception:
        # defensive: any unexpected error should fall back to simulation
        pass

    resp = simulate_ask(code, question)
    print(json.dumps(resp, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
