"""Demo: Ask sobre un archivo de código.

Carga `Demo/AcademyVerso/AcademyVerso_buggy.py`, inserta en prompt y simula respuestas.
"""
from pathlib import Path
import json

PROMPT_TEMPLATE = Path('prompts/ask_over_code_prompt.md').read_text(encoding='utf-8')
TARGET = Path('AcademyVerso/AcademyVerso_buggy.py')


def simulate_ask(code, question):
    # Simple heuristic: if question mentions 'eval', point to dangerous_eval; if 'sql', point to save_user_input
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
    # default
    return {
        'summary': 'El archivo contiene funciones para procesar valores, manejar config y ejecutar entradas del usuario.',
        'answer': 'No estoy seguro; ¿puedes preguntar sobre una parte concreta (p. ej. uso de eval o ejecución de comandos)?',
        'lines': []
    }


def main():
    code = TARGET.read_text(encoding='utf-8')
    question = input('Pregunta sobre el código: ').strip()
    prompt = PROMPT_TEMPLATE.replace('{{CODE}}', code).replace('{{QUESTION}}', question)
    print('--- Prompt enviado ---\n')
    print(prompt[:1000])
    print('\n--- Respuesta simulada ---\n')
    resp = simulate_ask(code, question)
    print(json.dumps(resp, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
