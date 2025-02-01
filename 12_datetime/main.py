# 12_datetime/main.py

# Пример 1: Использование модуля datetime
from datetime import datetime

now = datetime.now()
print("Текущее время:", now)

# Пример 2: Форматирование даты
formatted_date = now.strftime("%d.%m.%Y %H:%M:%S")
print("Форматированная дата:", formatted_date)

# Пример 3: Другой формат
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")  # Корректный формат
print("Форматированная дата:", formatted_date)