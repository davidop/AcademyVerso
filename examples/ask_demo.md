# Demo práctico: Ask (RAG)

Objetivo: mostrar cómo hacer preguntas sobre documentos cargados usando retrieval-augmented generation (RAG).

Pre-requisitos
- Python instalado.
- Opcional: vector DB o librería de embeddings si quieres una versión real.

Flujo
1) Contexto: explicar RAG brevemente (30s).
2) Ejecutar script de demo:

```powershell
py .\examples\ask_demo.py
```

3) Mostrar cómo el sistema selecciona documentos relevantes y genera una respuesta citando las fuentes.

Material incluido
- `examples/ask_demo.py` — script que indexa dos documentos en memoria, busca por similitud simple y devuelve respuesta con cita.
