# Demo práctico: Elegir el modelo AI correcto para tu tarea

Objetivo: comparar dos modelos representativos en términos de precisión, latencia y coste para una tarea de clasificación binaria simple.

Pre-requisitos
- Python (`py`) instalado para ejecutar el script de simulación (no requiere claves).
- Opcional: credenciales API si quieres adaptar el script a llamadas reales.

Flujo de la demo (8–10 minutos)

1) Contexto breve (1 min)
- Explica el caso de uso: clasificación binaria (p. ej. detectar intención "compra" vs "no compra" en mensajes).
- Presenta los dos modelos a comparar: `model-fast` (baja latencia, menor coste, precisión moderada) y `model-accurate` (mayor latencia y coste, mejor precisión).

2) Ejecutar el script de comparación (3–4 min)
- Desde la raíz del repo:

```powershell
py .\examples\choose_model_demo.py
```

- El script simula ejecutar ambos modelos en un conjunto de 10 ejemplos, mide latencia promedio, calcula precisión (accuracy), tokens estimados y coste estimado.

3) Interpretar resultados (2–3 min)
- Muestra la tabla resumen: Latencia avg, Accuracy, Tokens avg, Coste estimado.
- Discute trade-offs: cuándo preferir uno u otro según requisitos (SLA, presupuesto, criticidad).

4) Opcional: adaptar a llamadas reales
- Reemplaza la función `simulate_model` por una que haga llamadas a tu API (usa `API_KEY`, `API_URL`).

Material incluido
- `examples/choose_model_demo.py` — script de simulación.
