# 13_regex/main.py

# Пример 1: Поиск с помощью регулярных выражений
import re

text = "Мой номер телефона: +7-123-456-78-90"
pattern = r"\+\d-\d{3}-\d{3}-\d{2}-\d{2}"
match = re.search(pattern, text)
if match:
    print("Найден номер телефона:", match.group())

# Пример 2: Замена текста
new_text = re.sub(pattern, "[номер скрыт]", text)
print("Новый текст:", new_text)

# Пример 3: Ошибка из-за неправильного шаблона
# match = re.search(r"\d{10}", text)  # Не найдёт, так как шаблон не подходит
