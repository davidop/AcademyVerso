"""Demo Agent: simula un agente que llama a una API pública y procesa resultados.

Ejecuta:
  py .\examples\agent_demo.py

El script no requiere claves; usa una llamada simulada pero muestra logs y opción de abortar.
"""
import time
import threading


def simulated_api_call():
    print('[agent] Llamando a API pública: https://api.simulada.local/data')
    time.sleep(1.2)
    return {'title': 'Informe mensual', 'date': '2025-11-01', 'content': 'Resumen de métricas importantes...'}


def agent_run(abort_event):
    print('[agent] Inicio de ejecución')
    for step in range(1,4):
        if abort_event.is_set():
            print('[agent] Abortado por usuario antes del paso', step)
            return
        print(f'[agent] Paso {step}/3: ejecutando...')
        time.sleep(0.6)
    if abort_event.is_set():
        print('[agent] Abortado justo antes de la llamada a la API')
        return
    data = simulated_api_call()
    if abort_event.is_set():
        print('[agent] Abortado después de la llamada a la API')
        return
    print('[agent] Procesando datos...')
    time.sleep(0.8)
    print('[agent] Resultado:')
    print('  Título:', data['title'])
    print('  Fecha:', data['date'])
    print('  Contenido (excerpt):', data['content'])


def main():
    abort_event = threading.Event()
    t = threading.Thread(target=agent_run, args=(abort_event,))
    t.start()
    print('Presiona ENTER para abortar la ejecución en cualquier momento...')
    try:
        input()
        abort_event.set()
    except KeyboardInterrupt:
        abort_event.set()
    t.join()
    print('Ejecución terminada')


if __name__ == '__main__':
    main()
