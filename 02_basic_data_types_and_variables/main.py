# 02_basic_data_types_and_variables/main.py

# Пример 1: Целочисленный тип данных
x = 10
y = -5
print("x =", x, "| y =", y)

# Пример 2: Числа с плавающей точкой
pi = 3.14
temperature = -10.5
print("pi =", pi, "| temperature =", temperature)

# Пример 3: Строки
name = "Alice"
greeting = 'Hello, World!'
print(name, greeting)

# Пример 4: Логический тип данных
is_raining = True
is_sunny = False
print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)

# Пример 5: Динамическая типизация
x = 10
print("x is", x, "| type:", type(x))

x = "Hello"
print("x is", x, "| type:", type(x))

# Пример 6: Преобразование типов
x = "10"
y = int(x)  # Преобразуем строку в целое число
z = float(x)  # Преобразуем строку в число с плавающей точкой
print("y =", y, "| z =", z)

# Пример 7: Работа с переменными
a = 5
b = 10
a, b = b, a  # Обмен значениями
print("a =", a, "| b =", b)

# Пример 8: Ошибка из-за несовместимых типов
# x = 10
# y = "5"
# print(x + y)  # Ошибка: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Пример 9: Ошибка из-за неправильного преобразования
# x = "abc"
# y = int(x)  # Ошибка: ValueError: invalid literal for int() with base 10: 'abc'
