# Demo práctico: Modos de chat

Objetivo: demostrar conversaciones multi-turn, uso de mensajes de sistema para definir rol/tono y persistencia de contexto en una sesión.

Pre-requisitos
- Python (`py`) instalado para ejecutar el script de simulación.

Flujo de la demo (5–8 minutos)

1) Contexto (30s)
- Explica qué es un mensaje de sistema y por qué es útil (p. ej. establecer rol: "Eres un asistente técnico").

2) Ejecutar el script de demo (2–4 min)

```powershell
py .\examples\chat_modes_demo.py
```

- El script simula:
  - un mensaje de sistema que define el rol y tono,
  - dos intercambios usuario-assistente,
  - una instrucción posterior que cambia temporalmente el comportamiento.

3) Mostrar persistencia de contexto
- Explica cómo el asistente recuerda información del usuario dentro de la sesión (p. ej. nombre, preferencia de tono).

4) Mensajes clave
- Usa mensajes de sistema para consistencia de respuestas.
- Mantén el contexto relevante y evita incluir información sensible en el historial si no es necesario.

Material incluido
- `examples/chat_modes_demo.py` — script de demostración.
