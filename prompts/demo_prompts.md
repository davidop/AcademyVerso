# Prompts de Demo

## premium_request
Resumen largo del siguiente texto, 3 párrafos, tono formal:
<PEGA_TEXTO>

## choose_model_classification
Eres un experto en ML. Evalúa brevemente cuál de los modelos A o B es mejor para clasificación binaria en un dataset con 10k filas y 20 features. Considera latencia y coste.

## chat_mode_system
Eres un asistente técnico que responde en español con tono claro y conciso. Si no conoces la respuesta, indica los pasos para investigar.

## ask_rag
Has acceso a los siguientes documentos:
{{DOCUMENT_LIST}}
Responde la pregunta basándote en el contenido y cita la fuente.

## edits_text
Por favor mejora la claridad y concisión del siguiente párrafo, manteniendo el significado:
<TEXTO>

## agent_api
Eres un agente que puede llamar a una API pública; extrae el título y la fecha del artículo dado el endpoint.

## plan_mvp
Genera un plan en pasos para crear un MVP de una app de notas en 6 semanas.

## next_edit_suggestion
Sugiere la siguiente mejora para este archivo de documentación: <TEXTO>

## code_review
Revisa este fragmento de código y enumera posibles bugs, mejoras y problemas de seguridad:
<CODE>

## prompt_file_example
Usa el siguiente prompt template para crear un endpoint REST `POST /items` que valide entrada JSON y retorne 201:
{{TEMPLATE}}

## custom_chat_mode_support
Modo: Soporte Técnico. Mensaje de sistema: "Eres un asistente de soporte técnico con conocimiento en redes y Linux."

## copilot_example
Genera una función en Python que calcule el factorial de un número con manejo de errores y pruebas unitarias.

## mcp_tool_example
Describe cómo registrar un tool simple que llame a `GET /status` y devuelva JSON con `status`.
