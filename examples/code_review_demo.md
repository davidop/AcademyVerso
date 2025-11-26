# Demo práctico: Code Review

Objetivo: demostrar revisión automática de fragmentos de código, clasificación de hallazgos (bug, seguridad, estilo) y generación de acciones sugeridas (tests, fixes).

Pre-requisitos
- Python (`py`) instalado para ejecutar el script de simulación.

Flujo de la demo (6–10 minutos)

1) Presentar el PR o fragmento corto de código que se va a revisar.
2) Ejecutar el script de demo que analiza el código y produce comentarios categorizados.

```powershell
py .\examples\code_review_demo.py
```

3) Revisar los comentarios generados (bugs, seguridad, estilo) y aceptar/rechazar sugerencias.
4) Mostrar cómo generar tests sugeridos y aplicar cambios (manualmente o con PR patches).

Material incluido
- `examples/code_review_demo.py` — script que realiza una revisión simulada y muestra resultados estructurados.
