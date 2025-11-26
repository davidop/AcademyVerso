# Demo práctico: MCP (Model Context Protocol)

Objetivo: demostrar cómo exponer herramientas (tools) y contexto al modelo mediante MCP, registrar un tool simple y llamarlo desde el modelo de forma controlada.

Pre-requisitos
- Python (`py`) instalado.
- Entorno controlado para pruebas; la demo es totalmente local y simulada.

Flujo de la demo (6–10 minutos)

1) Contexto (1 min): explicar la arquitectura MCP — servidor de tools, registro, autorización y llamadas del modelo.

2) Ejecutar el script de demo:

```powershell
py .\examples\mcp_demo.py
```

3) Qué muestra el script:
- Registro de un tool llamado `status_checker` con un esquema simple.
- Simulación de una llamada del "modelo" al tool vía MCP, con verificación de autorización y logging.
- Ejemplo de respuesta del tool y cómo el modelo la integra en su output.

4) Discusión:
- Revisa controles de seguridad: validación de inputs, límites de permisos y auditoría de llamadas.
- Menciona cómo mapear esto a un entorno real (endpoints HTTP, autenticación basada en tokens y rate-limiting).

Material incluido
- `examples/mcp_demo.py` — script que simula un servidor MCP, registro de tool y llamada desde el modelo.
