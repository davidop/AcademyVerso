# Prompt: Crear endpoint REST en Flask

Instrucciones para el asistente:

- Crea un endpoint POST `/api/login` en Flask que acepte JSON con `username` y `password`.
- Valida entradas, maneja errores y devuelve JWT simulado en caso de éxito.
- Incluye pruebas unitarias con `pytest`.

Prompt:
```
Genera un endpoint POST `/api/login` en Flask que acepte JSON {"username": "", "password": ""}. Valida que los campos no estén vacíos, devuelve 400 con mensaje en caso de error. En caso correcto, devuelve 200 con JSON {"token":"<jwt>"} (puede ser un valor simulado). Incluye tests con pytest que cubran éxito y fallos.
```
