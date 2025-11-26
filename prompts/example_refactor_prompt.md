# Prompt de ejemplo para refactorizar código

Descripción: Mejora la legibilidad, aplica convenciones de estilo de Python (PEP8),
renombra variables crípticas y añade docstrings a funciones cuando sea apropiado.

Instrucciones:

- Mantén la misma funcionalidad.
- Si una variable tiene un nombre de 1 o 2 letras, cámbiala por un nombre más descriptivo.
- Añade docstrings a funciones que no los tengan.
- Mejora el formato (indentación, espacios alrededor de operadores, líneas en blanco).

Ejemplo corto:

```
Prompt: "Mejora nombres y formato, añade docstrings"

Input code:
def sum(a,b):
 return a+b

Output:
def sum_numbers(a: int, b: int) -> int:
    """Devuelve la suma de dos enteros."""
    return a + b
```

Uso: pasa el contenido de este archivo como `prompt` al llamar a `refactor_code`.
