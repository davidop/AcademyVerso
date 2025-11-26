"""Runner para prompt de code review.

Carga `AcademyVerso_buggy.py`, inserta su contenido en el prompt template y muestra una respuesta simulada en JSON.
"""
from pathlib import Path
import json

TEMPLATE = Path('prompts/code_review_prompt.md').read_text(encoding='utf-8')
TARGET = Path('AcademyVerso/AcademyVerso_buggy.py')


def simulate_review(code):
    # Este es un reporte simulado que coincide con las fallas intencionales
    report = {
        'file': str(TARGET),
        'findings': [
            {
                'type': 'security',
                'severity': 'high',
                'location': 'connect_db',
                'description': 'Credenciales hardcodeadas en el código.',
                'suggested_fix': "Usar variables de entorno o un gestor de secretos."
            },
            {
                'type': 'bug',
                'severity': 'high',
                'location': 'process_values',
                'description': 'Posible ZeroDivisionError y argumento por defecto mutable.',
                'suggested_fix': "Validar v != 0 y usar values=None por defecto."
            },
            {
                'type': 'security',
                'severity': 'critical',
                'location': 'dangerous_eval',
                'description': 'Uso de eval sobre input externo.',
                'suggested_fix': 'Reemplazar por ast.literal_eval o eliminar su uso.'
            },
            {
                'type': 'security',
                'severity': 'high',
                'location': 'run_shell',
                'description': 'Ejecución de comandos del usuario con os.system (inyección de comandos).',
                'suggested_fix': 'Validar/filtrar entrada o usar subprocess con argumentos.'
            },
            {
                'type': 'security',
                'severity': 'critical',
                'location': 'save_user_input',
                'description': 'Construcción de consulta SQL por concatenación (vulnerable a SQL injection).',
                'suggested_fix': 'Usar parámetros en la consulta: cur.execute(query, (name,)).'
            }
        ]
    }
    return report


def main():
    code = TARGET.read_text(encoding='utf-8')
    prompt = TEMPLATE.replace('{{CODE}}', code)
    print('--- Prompt enviado ---\n')
    print(prompt[:1000])
    print('\n--- Respuesta simulada (JSON) ---\n')
    report = simulate_review(code)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
