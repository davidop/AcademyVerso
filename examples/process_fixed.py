"""Implementación corregida y segura de la función `process` usada en la demo de code review.

La función evita división por cero, usa nombres descriptivos y es fácil de testear.
"""
from typing import List, Optional


def process(items: List[float]) -> List[Optional[float]]:
    """Procesa una lista de números y devuelve 10 / item para cada elemento.

    Para item == 0 devuelve None (evita división por cero).
    """
    result: List[Optional[float]] = []
    for item in items:
        if item == 0:
            result.append(None)
            continue
        result.append(10.0 / item)
    return result


if __name__ == '__main__':
    print(process([2,5,0]))
