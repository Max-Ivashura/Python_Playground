# Task 1
print(10 + 5)

# Task 2
x = 10
if x > 5:
    print("x > 5")

# Task 3
print(10 + 5 * 2)

# Task 4
try:
    num = int(input("Введите число:"))
    if num % 2 == 0:
        print("Чётное")
    else:
        print("Нечётное")
except ValueError:
    print("Ошибка: вы ввели не число!")

# Task 5
try:
    x = int(input("Введите число:"))
    if 5 < x < 10:
        print("Число больше 5 и меньше 10")
    else:
        print("Число не прошло проверку")
except ValueError:
    print("Ошибка: вы ввели не число!")
