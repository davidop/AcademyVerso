## Template: create_item_endpoint

Instrucciones: crea la especificación breve para un endpoint REST `POST /items` que valide el JSON de entrada usando el siguiente esquema:

```json
{
  "name": "string",
  "quantity": "integer >= 0",
  "price": "number >= 0"
}
```

Requisitos:
- Retorna `201` con el objeto creado en JSON cuando la validación pasa.
- Retorna `400` con mensaje de error si la validación falla.
- Incluye ejemplos de request y response.

Context variables:
- `{{SERVICE_NAME}}` - nombre del servicio
- `{{OWNER}}` - equipo responsable
