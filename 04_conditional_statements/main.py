# 04_conditional_statements/main.py

# Пример 1: Простое условие if
x = 10
if x > 5:
    print("x больше 5")

# Пример 2: Условие if-else
y = 3
if y > 5:
    print("y больше 5")
else:
    print("y меньше или равно 5")

# Пример 3: Условие if-elif-else
z = 7
if z > 10:
    print("z больше 10")
elif z > 5:
    print("z больше 5, но меньше или равно 10")
else:
    print("z меньше или равно 5")

# Пример 4: Тернарный оператор
result = "Чётное" if x % 2 == 0 else "Нечётное"
print("x является", result)

# Пример 5: Ошибка из-за отсутствия отступов
# if x > 5:
# print("x больше 5")  # Ошибка: IndentationError
