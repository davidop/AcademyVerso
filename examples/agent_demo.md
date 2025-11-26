# Demo práctico: Agent

Objetivo: demostrar un agente que ejecuta acciones externas (llamadas API), procesa resultados y reporta acciones con logs y posibilidad de abortar.

Pre-requisitos
- Python (`py`) instalado.
- Opcional: conexión a Internet si quieres que el agente llame una API real.

Flujo de la demo (6–10 minutos)

1) Explicar permisos y seguridad (30s):
- Los agentes que ejecutan acciones necesitan límites y autorización para evitar efectos secundarios.

2) Ejecutar el script de demo:

```powershell
py .\examples\agent_demo.py
```

3) Qué muestra el script:
- Registro de pasos (llamada API, parseo, resumen).
- Simulación de posibilidad de abortar la ejecución (presionando Enter durante la pausa) — en modo real implementa un control de cancelación.

4) Discusión:
- Cómo auditar acciones del agente y diseñar permisos mínimos.
- Cómo manejar errores y reintentos.

Material incluido
- `examples/agent_demo.py` — script de simulación con logs y paso abortable.
