# Demo práctico: Plan - Insiders

Objetivo: usar la funcionalidad "Plan" para generar un roadmap de proyecto y ajustar prioridades (feature Insider).

Pre-requisitos
- Acceso a la feature Plan (Insiders) si quieres integrar con la UI real.
- Python (`py`) instalado para ejecutar el script de ejemplo que simula la generación y edición de un plan.

Flujo de la demo (6–10 minutos)

1) Contexto (30s): explicar que la feature Plan genera pasos accionables y estimaciones.

2) Ejecutar el script:

```powershell
py .\examples\plan_demo.py
```

3) Qué hace el script:
- Genera automáticamente un plan de 6 semanas para un MVP de una app de notas.
- Permite editar prioridad de pasos (input) y exportar a `examples/tickets.csv`.

4) Mostrar exportación y cómo subir los tickets al gestor (Trello/Jira) — script crea CSV que puede importarse.

Material incluido
- `examples/plan_demo.py` — script de simulación que genera, permite editar prioridades y exporta tickets.
