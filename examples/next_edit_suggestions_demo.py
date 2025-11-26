"""Demo Next Edit Suggestions: sugiere mejoras y permite aplicarlas.

Ejecuta:
  py .\examples\next_edit_suggestions_demo.py
"""

ORIGINAL = (
    "El servicio necesita mejoras. Tenemos que revisar el rendimiento y asegurar que la experiencia de usuario sea la mejor posible. "
    "Tambien debemos considerar la seguridad y cumplimiento." 
)


SUGGESTIONS = [
    ('Mejorar precisión', 'Corregir acento y ampliar detalle sobre qué mejoras concretas se recomiendan.'),
    ('Añadir seguridad', 'Detallar medidas concretas: autenticación, logging y revisiones de dependencias.')
]


def apply_suggestion(text, suggestion):
    if suggestion[0] == 'Mejorar precisión':
        return text.replace('Tambien', 'También').replace('mejoras', 'mejoras de rendimiento y escalabilidad')
    if suggestion[0] == 'Añadir seguridad':
        return text + ' Recomendado: implementar autenticación robusta, logging centralizado y auditorías de dependencias.'
    return text


def main():
    print('--- Original ---')
    print(ORIGINAL)
    text = ORIGINAL
    for title, body in SUGGESTIONS:
        print('\nSugerencia:', title)
        print(body)
        ans = input('Aplicar sugerencia? (y/N): ').strip().lower()
        if ans == 'y':
            text = apply_suggestion(text, (title, body))
            print('Sugerencia aplicada.')
        else:
            print('Omitida.')
    print('\n--- Resultado final ---')
    print(text)


if __name__ == '__main__':
    main()
