# Prompt por defecto para EditChat

Descripción: Aplica mejoras automáticas a código Python para esta demo.

Objetivos:

- Mejorar nombres de variables cortas o crípticas.
- Añadir docstrings a funciones públicas sin cambiar la funcionalidad.
- Aplicar formato PEP8 básico (espacios, indentación, separación entre funciones).
- Evitar cambios semánticos, mantener compatibilidad.

Instrucciones de uso:

- Este prompt se usará automáticamente por `Edit.py` cuando no se especifique otro prompt.
- Si alguna transformación es ambigua, preferir cambios conservadores.

Ejemplo breve:

Input:
```
def sum(a,b):
 return a+b
```

Output esperado:
```
def sum_numbers(a: int, b: int) -> int:
    """Devuelve la suma de dos enteros."""
    return a + b
```
