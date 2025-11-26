"""Simulación de flujos de GitHub Copilot para demo.

Ejecuta:
  py .\examples\copilot_demo.py
"""

def simulate_autocomplete():
    print('--- Autocomplete in-line ---')
    print('Input: def factorial(n):')
    print('Suggestion:')
    print('''def factorial(n):\n    if n < 0: raise ValueError('n must be >= 0')\n    res = 1\n    for i in range(2, n+1):\n        res *= i\n    return res''')


def simulate_generate_tests():
    print('\n--- Generar tests desde comentario ---')
    print('Comment: # genera tests para factorial')
    print('Suggested tests:')
    print('''def test_factorial_zero(): assert factorial(0) == 1\ndef test_factorial_positive(): assert factorial(5) == 120\ndef test_factorial_negative(): raises ValueError''')


def simulate_pr_assist():
    print('\n--- Asistencia en PR ---')
    print('Suggested review comments:')
    print('- Añadir manejo de errores para entrada negativa')
    print('- Añadir tests para casos límite y performance')


def main():
    simulate_autocomplete()
    simulate_generate_tests()
    simulate_pr_assist()


if __name__ == '__main__':
    main()
