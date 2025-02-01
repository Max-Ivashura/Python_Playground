# 05_loops/main.py

# Пример 1: Цикл for
print("1.For")
for i in range(5):  # range(5) генерирует числа от 0 до 4
    print("i =", i)

# Пример 2: Цикл while
print("2.While")
x = 0
while x < 5:
    print("x =", x)
    x += 1

# Пример 3: Управление циклами (break, continue)
print("3.Break and Continue")
for i in range(10):
    if i == 3:
        continue  # Пропустить текущую итерацию
    if i == 7:
        break  # Выйти из цикла
    print("i =", i)

# Пример 4: Ошибка из-за бесконечного цикла
# x = 0
# while x < 5:  # Если не увеличивать x, цикл будет бесконечным
#     print("x =", x)
