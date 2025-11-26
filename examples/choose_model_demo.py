"""Script de ejemplo para comparar dos modelos en una tarea de clasificación.

Ejecuta:
  py .\examples\choose_model_demo.py

El script simula predicciones de dos modelos y mide latencia, precisión y coste estimado.
"""
import time
import random


TEST_SET = [
    ('Cliente solicita información de precio', 1),
    ('Mensaje de felicitación sin intención de comprar', 0),
    ('Quiero comprar ahora mismo', 1),
    ('Consulta técnica sobre características', 0),
    ('¿Dónde puedo comprar?', 1),
    ('Gracias por la ayuda', 0),
    ('Necesito una factura', 1),
    ('Solo curioseando', 0),
    ('Me interesa la oferta', 1),
    ('No estoy interesado', 0),
]


def simulate_model(text, model_name):
    """Simula respuesta de modelo: devuelve etiqueta 0/1 y tokens usados."""
    # model-fast: más rápido, menos preciso
    if model_name == 'model-fast':
        time.sleep(0.05 + random.random() * 0.05)
        # accuracy ~80%
        pred = random.choices([0,1], weights=[0.55,0.45])[0]
        tokens = random.randint(20,40)
        cost = tokens * 0.00001
    else:
        # model-accurate: más lento, más preciso
        time.sleep(0.12 + random.random() * 0.08)
        pred = random.choices([0,1], weights=[0.45,0.55])[0]
        tokens = random.randint(30,60)
        cost = tokens * 0.00002
    return pred, tokens, cost


def evaluate_model(model_name):
    total = len(TEST_SET)
    correct = 0
    tokens_total = 0
    cost_total = 0.0
    times = []
    for text, label in TEST_SET:
        start = time.time()
        pred, tokens, cost = simulate_model(text, model_name)
        elapsed = time.time() - start
        times.append(elapsed)
        tokens_total += tokens
        cost_total += cost
        if pred == label:
            correct += 1
    accuracy = correct / total
    avg_latency = sum(times) / len(times)
    avg_tokens = tokens_total / total
    return {
        'model': model_name,
        'accuracy': accuracy,
        'avg_latency_s': avg_latency,
        'avg_tokens': avg_tokens,
        'cost_estimated': cost_total,
    }


def main():
    r1 = evaluate_model('model-fast')
    r2 = evaluate_model('model-accurate')
    print('--- Resultados ---')
    for r in (r1, r2):
        print(f"Modelo: {r['model']}")
        print(f"  Accuracy: {r['accuracy']*100:.1f}%")
        print(f"  Latencia media: {r['avg_latency_s']*1000:.1f} ms")
        print(f"  Tokens promedio: {r['avg_tokens']:.1f}")
        print(f"  Coste estimado total (muestra): ${r['cost_estimated']:.6f}")
        print('')
    print('Interpretación: elige `model-fast` para baja latencia y coste; `model-accurate` para mayor precisión en tareas críticas.')


if __name__ == '__main__':
    main()
