# Demo práctico: Premium Requests

Objetivo: mostrar la diferencia en prioridad, latencia y calidad entre una petición estándar y una petición premium.

Pre-requisitos
- Tener una clave API con acceso premium (no exponerla en pantalla).
- Tener `py`/`python` instalado o disponer de `curl`/PowerShell.
- Acceso al dashboard de métricas del proveedor para mostrar uso y coste.

Flujo de la demo (10 minutos aprox.)

1) Preparar prompt y texto de ejemplo (cópialo):

```
Resumen largo del siguiente texto, 3 párrafos, tono formal:

El contrato establece que la parte A se obliga a entregar los componentes descritos en el Anexo I en un plazo máximo de noventa (90) días naturales desde la firma del presente documento. En caso de retrasos imputables a la parte A, se aplicarán las penalizaciones previstas en la cláusula 7, sin perjuicio de la facultad de la parte contratante de resolver el contrato si el retraso supera los sesenta (60) días. Además, la parte A deberá mantener la confidencialidad de toda la información técnica entregada por la parte contratante, conforme a lo dispuesto en la cláusula 12.
```

2) Medir latencia y tokens con PowerShell (ejemplo de comandos)

- Usando `curl` con variable de entorno `API_KEY` y `API_URL` (reemplazar por tu endpoint):

```powershell
$env:API_KEY = 'tu_api_key_aqui'
$env:API_URL = 'https://api.tu-proveedor.com/v1/responses'

# Petición estándar
Measure-Command { 
  curl -s -X POST $env:API_URL -H "Authorization: Bearer $env:API_KEY" -H "Content-Type: application/json" -d (@"{
    "model": "tu-modelo",
    "input": "Resumen largo del siguiente texto, 3 párrafos, tono formal: <PEGA_TEXTO>"
  }"@)
}

# Petición premium (ejemplo: query param premium=true o header X-Priority)
Measure-Command { 
  curl -s -X POST "$env:API_URL?premium=true" -H "Authorization: Bearer $env:API_KEY" -H "Content-Type: application/json" -d (@"{
    "model": "tu-modelo",
    "input": "Resumen largo del siguiente texto, 3 párrafos, tono formal: <PEGA_TEXTO>"
  }"@)
}
```

Notas:
- `Measure-Command` devuelve tiempo de ejecución; repite cada llamada 3 veces y promedia.
- Muchos proveedores incluyen en la respuesta un campo `usage` con `prompt_tokens` y `completion_tokens` — muéstralo en la demo para comparar coste.

3) Ejemplo con Python (script de ejemplo)

- Ejecuta el script `examples/premium_request_demo.py` con `py .\examples\premium_request_demo.py`.
- El script hace dos llamadas (estándar y premium), mide tiempo y muestra longitud de la respuesta. Requiere la variable `API_KEY` y `API_URL`.

4) Comparar calidad

- Muestra las dos respuestas (estándar vs premium) y resalta diferencias en:
  - coherencia del texto
  - preservación de términos legales
  - longitud y fluidez

5) Mostrar dashboard

- Abre el dashboard del proveedor y busca métricas de las peticiones realizadas: latencia, tokens consumidos y coste.
- Explica límites de uso (rate limits) y cómo el plan premium cambia priorización o cuota.

6) Mensajes clave para la audiencia

- Premium = mejor prioridad y a menudo menor latencia; justificar por SLAs.
- Evalúa coste vs beneficio: usar premium en tareas críticas (legal, financiero, producción).
- Tener métricas y alertas para detectar anomalías y evitar costes inesperados.

Material de apoyo
- Archivo de prompt de ejemplo: `prompts/demo_prompts.md` (clave `premium_request`).
- Script de demostración: `examples/premium_request_demo.py`.
