# Demos - Instrucciones de ejecución

Este repositorio contiene demos prácticas para presentar funcionalidades de IA. Cada demo tiene una guía (`.md`) y un script en `examples/`.

Requisitos generales
- Python 3 instalado (`py` en Windows). Si no lo tienes, instala desde https://www.python.org/downloads/.
- Opcional: claves API y endpoints para ejecutar llamadas reales (varía por demo).

Estructura relevante
- `docs/DEMO_GUIDE.md` — guía principal de las demos.
- `prompts/` — prompts y templates reutilizables.
- `examples/` — scripts y guías para cada demo.

Cómo ejecutar un demo

1. Abre PowerShell en la carpeta raíz del repo.
2. Ejecuta el script deseado. Ejemplos:

```powershell
py .\examples\premium_request_demo.py
py .\examples\choose_model_demo.py
py .\examples\chat_modes_demo.py
py .\examples\ask_demo.py
py .\examples\edits_demo.py
py .\examples\agent_demo.py
py .\examples\plan_demo.py
py .\examples\next_edit_suggestions_demo.py
py .\examples\code_review_demo.py
py .\examples\prompt_files_demo.py
py .\examples\custom_chat_modes_demo.py
py .\examples\copilot_demo.py
py .\examples\mcp_demo.py
```

Detalles por demo

- Premium Requests:
  - Archivo guía: `examples/premium_request_demo.md`.
  - Script: `examples/premium_request_demo.py` (simula respuestas si no hay `API_KEY` y `API_URL`).
  - Para pruebas reales exporta en PowerShell:
    ```powershell
    $env:API_KEY = 'sk-...'
    $env:API_URL = 'https://api.tu-proveedor.com/v1/responses'
    py .\examples\premium_request_demo.py
    ```

- Choosing the right AI model:
  - Archivo guía: `examples/choose_model_demo.md`.
  - Script: `examples/choose_model_demo.py` (simula accuracy, latencia y coste).

- Modos de chat:
  - Archivo guía: `examples/chat_modes_demo.md`.
  - Script: `examples/chat_modes_demo.py` (simula conversación multi-turn y mensaje de sistema).

- Ask (RAG):
  - Archivo guía: `examples/ask_demo.md`.
  - Script: `examples/ask_demo.py` (indexa documentos en memoria y responde preguntas por similitud).

- Edits:
  - Archivo guía: `examples/edits_demo.md`.
  - Script: `examples/edits_demo.py` (aplica ediciones simuladas: formal y conciso).

- Agent:
  - Archivo guía: `examples/agent_demo.md`.
  - Script: `examples/agent_demo.py` (simula pasos de agente, llamada API y opción de abortar presionando Enter).

- Plan - Insiders:
  - Archivo guía: `examples/plan_demo.md`.
  - Script: `examples/plan_demo.py` (genera plan de 6 semanas, permite editar prioridades y exportar `examples/tickets.csv`).

- Next Edit Suggestions:
  - Archivo guía: `examples/next_edit_suggestions_demo.md`.
  - Script: `examples/next_edit_suggestions_demo.py` (genera sugerencias y permite aplicarlas).

- Code Review:
  - Archivo guía: `examples/code_review_demo.md`.
  - Script: `examples/code_review_demo.py` (revisión simulada: bug, estilo, tests faltantes).

- Prompt Files:
  - Template: `prompts/prompt_files_demo.md`.
  - Archivo guía: `examples/prompt_files_demo.md`.
  - Script: `examples/prompt_files_demo.py` (carga template y reemplaza variables).

- Custom Chat Modes:
  - Archivo guía: `examples/custom_chat_modes_demo.md`.
  - Script: `examples/custom_chat_modes_demo.py` (define un modo y lo guarda como JSON).

- Copilot en GitHub:
  - Archivo guía: `examples/copilot_demo.md`.
  - Script: `examples/copilot_demo.py` (simula completados y generación de tests).

- MCP:
  - Archivo guía: `examples/mcp_demo.md`.
  - Script: `examples/mcp_demo.py` (simula registro de tool y llamada desde el modelo).

Buenas prácticas durante la demo

- No mostrar claves en pantalla; usa variables de entorno.
- Ten capturas o clips listos como plan B si una demo en vivo falla.
- Repite mediciones (latencia/tokens) varias veces y promedia.

¿Quieres que cree un `run_all_demos.ps1` que ejecute todos los scripts secuencialmente (con pausas entre ellos)?
