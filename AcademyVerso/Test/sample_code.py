"""Código de ejemplo para generar tests en la demo.

Contiene varias funciones de propósito general con comportamientos simples
que sirven para demostrar la generación de tests unitarios.
"""

from typing import List


def add(a: float, b: float) -> float:
    """Devuelve la suma de `a` y `b`."""
    return a + b


def multiply(values: List[float]) -> float:
    """Devuelve el producto de todos los elementos en `values`.

    Si la lista está vacía, devuelve 1.0 (identidad multiplicativa).
    """
    result = 1.0
    for v in values:
        result *= v
    return result


def divide(a: float, b: float) -> float:
    """Divide `a` entre `b`.

    Lanza `ZeroDivisionError` si `b` es 0.
    """
    return a / b


def is_prime(n: int) -> bool:
    """Devuelve True si `n` es un número primo (n >= 2), False en otro caso."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def factorial(n: int) -> int:
    """Calcula el factorial de `n` para n >= 0. Lanza ValueError si n < 0."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
