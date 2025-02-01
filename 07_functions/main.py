# 07_functions/main.py

# Пример 1: Простая функция
def greet(name):
    return f"Привет, {name}!"


print(greet("Alice"))


# Пример 2: Функция с аргументами по умолчанию
def power(x, n=2):
    return x ** n


print("2 в степени 3:", power(2, 3))
print("2 в квадрате:", power(2))

# Пример 3: Лямбда-функция
square = lambda x: x ** 2
print("Квадрат числа 5:", square(5))

# Пример 4: Ошибка из-за отсутствия return
# def add(a, b):
#     result = a + b
# print(add(2, 3))  # Ошибка: None, так как функция ничего не возвращает
