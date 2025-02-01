# 16_libraries/main.py

# Пример 1: Использование библиотеки requests
import requests

response = requests.get("https://api.github.com")
print("Статус код:", response.status_code)

# Пример 2: Использование библиотеки numpy
import numpy as np

array = np.array([1, 2, 3])
print("Массив numpy:", array)

# Пример 3: Ошибка из-за отсутствия библиотеки
# import nonexistent_library  # Ошибка: ModuleNotFoundError