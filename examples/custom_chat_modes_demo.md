# Demo práctico: Custom Chat Modes

Objetivo: crear y usar modos de chat personalizados con mensajes de sistema por defecto (rol y tono), y compartirlos con el equipo.

Pre-requisitos
- Acceso a la UI/API que permita crear chat modes si quieres persistirlos; el ejemplo usa un script simulado.

Flujo de la demo (4–6 minutos)

1) Explicar qué es un Custom Chat Mode: mensajes de sistema + configuración de tono y comportamiento.
2) Ejecutar el script de demo:

```powershell
py .\examples\custom_chat_modes_demo.py
```

3) El script mostrará:
- Definición de un modo "Soporte Técnico" con mensajes de sistema.
- Una conversación de ejemplo usando ese modo.
- Cómo exportar/importar el modo (simulado como JSON local).

4) Discusión: gobernanza de modos, control de versiones y privacidad (no incluir secretos en mensajes de sistema).

Material incluido
- `examples/custom_chat_modes_demo.py` — script de ejemplo que crea y aplica un modo de chat.
