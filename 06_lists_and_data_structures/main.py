# 06_lists_and_data_structures/main.py

# Пример 1: Списки
numbers = [1, 2, 3, 4, 5]
print("Список numbers:", numbers)

# Пример 2: Индексация и срезы
print("Первый элемент:", numbers[0])  # Индексация начинается с 0
print("Срез списка:", numbers[1:4])  # Элементы с индексом 1 до 3

# Пример 3: Кортежи
coordinates = (10, 20)
print("Координаты:", coordinates)

# Пример 4: Множества
unique_numbers = {1, 2, 2, 3, 3, 4}
print("Множество unique_numbers:", unique_numbers)

# Пример 5: Словари
person = {"name": "Alice", "age": 25}
print("Словарь person:", person)

# Пример 6: Ошибка из-за несуществующего ключа
# print(person["height"])  # Ошибка: KeyError: 'height'
