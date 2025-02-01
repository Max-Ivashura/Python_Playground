# 10_modules_and_packages/main.py

# Пример 1: Импорт модуля
import math

print("Квадратный корень из 16:", math.sqrt(16))

# Пример 2: Импорт конкретной функции
from random import randint

print("Случайное число:", randint(1, 10))

# Пример 3: Создание собственного модуля
# Создайте файл my_module.py с функцией greet()
import my_module
my_module.greet("Alice")

# Пример 4: Ошибка из-за отсутствия модуля
# import nonexistent_module  # Ошибка: ModuleNotFoundError
