# Guía de Demos - AI Features

Esta guía contiene instrucciones prácticas y reproducibles para demo de características clave: Premium Requests, elección de modelo, modos de chat, Ask, Edits, Agent, Plan (Insiders), Next Edit Suggestions, Code Review, Prompt Files, Custom Chat Modes, Copilot en GitHub y MCP.

Formato general de cada demo

- Objetivo: una frase clara sobre lo que se demuestra.
- Audiencia: técnica / no técnica.
- Pre-requisitos: credenciales, accesos y recursos necesarios.
- Duración sugerida: 5–10 minutos.
- Flujo: contexto breve → mostrar UI/CLI → ejecutar 1–2 casos reales → discutir resultados y límites.
- Checklist técnico: prompts listos, comandos copiable, variables de entorno, plan B (screenshots/video).

1) Premium Requests

- Objetivo: mostrar diferencia en prioridad, latencia y calidad.
- Pre-requisitos: clave con acceso premium y dashboard de métricas.
- Pasos de demo:
  1. Ejecutar la misma petición con y sin premium y comparar latencia/tokens.
  2. Mostrar una tarea crítica (ej.: resumen largo o generación legal) y comparar salida.
  3. Mostrar límites de uso y coste estimado en el dashboard.
- Prompt ejemplo (cópialo):

```
Resumen largo del siguiente texto, 3 párrafos, tono formal:
<PEGA_TEXTO>
```

2) Choosing the right AI model for your task

- Objetivo: elegir modelo por costo, latencia y capacidad.
- Pre-requisitos: lista de modelos y ejemplos de benchmark.
- Pasos:
  1. Definir caso de uso (clasificación, generación larga, código, visión).
  2. Probar 2 modelos representativos y comparar precisión y coste.
  3. Documentar trade-offs: tokens máximos, latencia, temperatura.

3) Modos de chat

- Objetivo: demostrar conversaciones multi-turn y mensajes de sistema.
- Pre-requisitos: UI o cliente que permita mensajes de sistema.
- Pasos:
  1. Mostrar chat normal (usuario ↔ assistant).
  2. Añadir mensaje de sistema: `Eres un asistente experto en X`.
  3. Mostrar cómo mantener y reutilizar contexto en la sesión.

4) Ask

- Objetivo: preguntas directas y QA con retrieval (RAG).
- Pre-requisitos: documentos cargados o Vector DB configurado.
- Pasos:
  1. Pregunta simple y respuesta.
  2. QA sobre documento: cargar documento y hacer preguntas específicas.
  3. Validar respuestas y discutir riesgos de alucinaciones.

5) Edits

- Objetivo: editar texto o código mediante instrucciones.
- Pre-requisitos: endpoint o editor con soporte de edits.
- Pasos:
  1. Editar un párrafo: "hazlo más formal y conciso".
  2. Editar código: pedir refactorizar una función pequeña y mostrar diff.
  3. Ajustar parámetros (p. ej. temperatura baja para cambios conservadores).

6) Agent

- Objetivo: demostrar agentes que ejecutan acciones (API, búsquedas, comandos).
- Pre-requisitos: entorno controlado y conectores básicos.
- Pasos:
  1. Explicar permisos y límites.
  2. Demo: agente consulta una API pública, procesa datos y retorna resumen.
  3. Mostrar logs de acciones y la posibilidad de abortar.

7) Plan - Insiders

- Objetivo: generar pasos automáticos para planificación (disponible en Insiders).
- Pre-requisitos: cuenta Insider con acceso a la feature.
- Pasos:
  1. Pedir al Plan que genere un roadmap para un MVP.
  2. Ajustar prioridades y exportar a tickets.

8) Next Edit Suggestions

- Objetivo: sugerencias contextuales dentro del editor.
- Pre-requisitos: integración con editor (VS Code o web).
- Pasos:
  1. Activar sugerencias en un archivo y aplicar una sugerencia.
  2. Revisar el diff y aceptar/rechazar.

9) Code Review

- Objetivo: revisar PRs automáticamente y generar comentarios accionables.
- Pre-requisitos: repo con PR o commits y herramientas de integración.
- Pasos:
  1. Ejecutar revisión automática en un PR pequeño.
  2. Clasificar hallazgos (bug, seguridad, estilo) y generar tests sugeridos.

10) Prompt Files

- Objetivo: organizar prompts en archivos reutilizables y versionables.
- Pre-requisitos: carpeta `prompts/` en el repo (ej.: `prompts/create_endpoint.md`).
- Pasos:
  1. Guardar prompt en `prompts/` y usar variables para personalizar.
  2. Cargar el prompt desde un script o UI y ejecutar.

Ejemplo de uso desde Python (pseudo-código):

```
# cargar archivo prompt
with open('prompts/create_endpoint.md') as f:
    prompt = f.read()
# reemplazar variables
prompt = prompt.replace('{{ENTITY}}', 'usuario')
# llamar API con prompt
response = client.create_chat_completion(prompt)
```

11) Custom Chat Modes

- Objetivo: crear modos de chat con instrucciones por defecto (p. ej. Soporte Técnico).
- Pre-requisitos: UI/API que permita guardar chat modes.
- Pasos:
  1. Definir mensajes de sistema y tono.
  2. Guardar modo y compartir con el equipo.

12) Copilot en GitHub.com

- Objetivo: demostrar autocompletado, generación de tests y asistencia en PRs.
- Pre-requisitos: cuenta GitHub con Copilot habilitada.
- Pasos:
  1. Mostrar completado in-line en editor web o VS Code.
  2. Generar tests desde comentarios y aplicar cambios.

13) MCP (Model Context Protocol)

- Objetivo: enseñar cómo exponer herramientas y contexto al modelo mediante MCP.
- Pre-requisitos: servidor MCP o entorno MCP-enabled, ejemplo de connector.
- Pasos:
  1. Explicar arquitectura MCP y sus componentes.
  2. Registrar un tool simple y llamar desde el modelo.
  3. Revisar autorizaciones y validaciones de entrada.

Buenas prácticas para las demos

- Variables de entorno: nunca muestres claves; usa `export`/`setx` o variables en el runner.
- Logs y métricas: captura latencia, tokens y coste estimado.
- Plan B: tener capturas o clips si la demo en vivo falla.
- Reproducibilidad: incluye prompts exactos, comandos y un script de ejemplo.

Archivos sugeridos a añadir al repo

- `docs/DEMO_GUIDE.md` (este archivo)
- `prompts/*.md` (prompts por caso de uso)
- `examples/demo_runner.py` (scripts que ejecuten llamadas mínimas reproducibles)
- `examples/README.md` con pasos para ejecutar las demos localmente

¿Quieres que añada ahora un `examples/demo_runner.py` con ejemplos básicos y un `prompts/demo_prompts.md` para empezar? Si confirmas, los creo y actualizo el TODO.
