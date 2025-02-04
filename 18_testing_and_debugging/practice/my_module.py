def add(a, b):
    """Функция складывает два числа."""
    return a + b


def is_even(n):
    """Функция проверяет, является ли число четным."""
    return n % 2 == 0


def factorial(n):
    """Функция вычисляет факториал числа."""
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def greet(name):
    """Функция возвращает строку приветствия."""
    return f"Привет, {name}!"


def divide(a, b):
    """Функция делит одно число на другое, обрабатывая деление на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b
