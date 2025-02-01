# 15_decorators/main.py

# Пример 1: Простой декоратор
def my_decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Привет!")

say_hello()

# Пример 2: Декоратор с аргументами
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Привет!")

say_hi()

# Пример 3: Ошибка из-за неправильного использования декоратора
# @my_decorator
# def add(a, b):
#     return a + b
# print(add(2, 3))  # Ошибка: wrapper() не принимает аргументы