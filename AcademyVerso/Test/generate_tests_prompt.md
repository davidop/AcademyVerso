# Prompt para generar tests con pytest

Eres un asistente que genera tests automáticos usando `pytest`.

Tarea:
- Escribe una suite de tests para el archivo `sample_code.py` en la misma carpeta.
- Crea tests que cubran casos normales, bordes y errores esperados.
- Usa `pytest` y escribe las pruebas en un archivo llamado `test_sample_code.py`.
- Cada test debe ser lo más claro posible y usar `assert` para las comprobaciones.
- No modifiques `sample_code.py`.

Requisitos específicos:
- Prueba `add` con números positivos, negativos y floats.
- Prueba `multiply` con lista vacía, lista con ceros, y lista normal.
- Prueba `divide` con divisor no nulo y con `b=0` para asegurar `ZeroDivisionError`.
- Prueba `is_prime` con varios valores (0,1,2, primes, composites).
- Prueba `factorial` con valores 0, 1, 5 y asegúrate de que `ValueError` se lanza para valores negativos.

Formato de salida esperado:
- Devuelve solo el contenido del archivo `test_sample_code.py` sin explicaciones.
