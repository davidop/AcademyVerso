"""Script de ejemplo para la demo de Premium Requests.

Uso (PowerShell):
  py .\examples\premium_request_demo.py

El script funciona en modo `simulate` por defecto. Para usar la API real, exporta `API_KEY` y `API_URL`.
"""
import os
import time
import json
import requests


API_KEY = os.environ.get('API_KEY')
API_URL = os.environ.get('API_URL')


PROMPT = (
    "Resumen largo del siguiente texto, 3 párrafos, tono formal:\n\n"
    "El contrato establece que la parte A se obliga a entregar los componentes descritos en el Anexo I en un plazo máximo de noventa (90) días naturales desde la firma del presente documento. "
    "En caso de retrasos imputables a la parte A, se aplicarán las penalizaciones previstas en la cláusula 7, sin perjuicio de la facultad de la parte contratante de resolver el contrato si el retraso supera los sesenta (60) días. "
    "Además, la parte A deberá mantener la confidencialidad de toda la información técnica entregada por la parte contratante, conforme a lo dispuesto en la cláusula 12."
)


def call_api(prompt, premium=False):
    """Llama al endpoint si API_KEY y API_URL están presentes, si no simula respuesta."""
    if not API_KEY or not API_URL:
        return simulate_response(prompt, premium)

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    params = {'premium': 'true'} if premium else {}
    payload = {
        'model': 'tu-modelo',
        'input': prompt
    }
    start = time.time()
    resp = requests.post(API_URL, headers=headers, params=params, json=payload, timeout=60)
    elapsed = time.time() - start
    try:
        body = resp.json()
    except Exception:
        body = {'text': resp.text}
    return {'elapsed': elapsed, 'body': body}


def simulate_response(prompt, premium=False):
    """Genera una respuesta simulada con ligera diferencia entre premium/no premium."""
    base = (
        "Resumen (simulado): La parte A se compromete a entregar los componentes en 90 días. "
        "Si hay retrasos, aplican las penalizaciones y la parte contratante puede resolver el contrato si el retraso supera 60 días. "
        "La confidencialidad se mantiene según la cláusula correspondiente."
    )
    if premium:
        # premium: respuesta más elaborada
        text = base + " [RESPUESTA PREMIUM: mayor detalle legal y redacción pulida.]"
    else:
        text = base + " [RESPUESTA ESTÁNDAR: versión más concisa.]"
    # Simulate elapsed time difference
    elapsed = 0.8 if premium else 1.4
    body = {
        'text': text,
        'usage': {'prompt_tokens': 120, 'completion_tokens': 200 if premium else 180}
    }
    return {'elapsed': elapsed, 'body': body}


def run_demo():
    print('Demo Premium Requests - inicio')
    print('Prompt utilizado:\n')
    print(PROMPT)

    print('\nLlamada ESTÁNDAR...')
    r1 = call_api(PROMPT, premium=False)
    print(f"Tiempo: {r1['elapsed']:.3f}s")
    print('Tokens (estimado):', r1['body'].get('usage'))
    print('Respuesta:\n', r1['body'].get('text'))

    print('\nLlamada PREMIUM...')
    r2 = call_api(PROMPT, premium=True)
    print(f"Tiempo: {r2['elapsed']:.3f}s")
    print('Tokens (estimado):', r2['body'].get('usage'))
    print('Respuesta:\n', r2['body'].get('text'))

    print('\nComparación:')
    print(f"Diferencia de latencia: {r1['elapsed'] - r2['elapsed']:.3f}s (estándar - premium)")
    print('Diferencia en tokens:', r1['body'].get('usage'), 'vs', r2['body'].get('usage'))

    print('\nFin demo. Abre tu dashboard para ver métricas y coste real.')


if __name__ == '__main__':
    run_demo()
