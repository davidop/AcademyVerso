"""Demo MCP: simula registro de un tool y llamada desde el modelo.

Ejecuta:
  py .\examples\mcp_demo.py
"""
import time


TOOLS = {}


def register_tool(name, schema):
    TOOLS[name] = {'schema': schema, 'registered_at': time.time()}
    print(f'[mcp] Tool registrado: {name}')


def call_tool(name, params, authorized=True):
    print(f'[mcp] Llamada a tool {name} con params: {params}')
    if not authorized:
        return {'error': 'not_authorized'}
    # Simulate tool behavior
    if name == 'status_checker':
        return {'status': 'ok', 'uptime': '48 days', 'services': ['db','api','web']}
    return {'error': 'unknown_tool'}


def main():
    register_tool('status_checker', {'type': 'GET', 'path': '/status'})
    print('\nSimulando llamada desde el modelo...')
    resp = call_tool('status_checker', {}, authorized=True)
    print('[mcp] Respuesta del tool:', resp)


if __name__ == '__main__':
    main()
