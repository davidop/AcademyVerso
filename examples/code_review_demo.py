"""Demo Code Review: analiza un fragmento de código y genera comentarios simulados.

Ejecuta:
  py .\examples\code_review_demo.py
"""

CODE = '''
def process(items):
    result = []
    for i in items:
        result.append(10 / i)
    return result
'''


def analyze(code):
    findings = []
    if '10 / i' in code:
        findings.append({'type': 'bug', 'message': 'Posible división por cero al iterar elementos.'})
    if 'for i in items' in code:
        findings.append({'type': 'style', 'message': 'Usar nombres de variables más descriptivos (i → item).'} )
    if 'result = []' in code and 'append' in code:
        findings.append({'type': 'performance', 'message': 'Considerar comprensión de lista para mayor rendimiento.'})
    findings.append({'type': 'tests', 'message': 'Falta test para caso con item = 0 y lista vacía.'})
    return findings


def main():
    print('--- Código a revisar ---')
    print(CODE)
    findings = analyze(CODE)
    print('\n--- Hallazgos ---')
    for f in findings:
        print(f"[{f['type'].upper()}] {f['message']}")

    print('\nSugerencia de parche: ver examples/process_fixed.py para una implementación segura y tests en tests/test_process.py')


if __name__ == '__main__':
    main()
