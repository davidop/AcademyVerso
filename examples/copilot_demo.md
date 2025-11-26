# Demo práctico: Copilot en GitHub

Objetivo: demostrar flujos comunes de GitHub Copilot: autocompletado in-line, generación de tests desde comentarios y asistencia en PRs.

Pre-requisitos
- Cuenta GitHub con Copilot habilitado (para demo en vivo).
- Acceso al repositorio y un PR o archivo abierto en el editor (web o VS Code).

Flujo de la demo (5–8 minutos)

1) Mostrar autocompletado in-line
- Abre un archivo y escribe un comentario o un esqueleto de función. Copilot sugiere el completado; acepta o edita la sugerencia.

2) Generar tests desde un comentario
- Escribe un comentario `# genera tests para la función foo` y muestra cómo Copilot sugiere casos de prueba.

3) Asistencia en PRs
- Muestra cómo Copilot/Code Review puede sugerir cambios o tests para un PR; enumera los comentarios sugeridos.

Material incluido
- `examples/copilot_demo.py` — script simulador que muestra ejemplos de completados generados y tests propuestos.

Notas
- No expongas claves ni datos privados durante la demo. Si la demo en vivo falla, usa las salidas simuladas del script.
