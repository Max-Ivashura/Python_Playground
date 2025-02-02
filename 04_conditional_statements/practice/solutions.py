# Task 1
try:
    num = int(input("Введите число: "))
    if num > 5:
        print("Число больше 5!")
    else:
        print("Число не больше 5!")
except ValueError:
    print("Ошибка! Вы ввели не число!")

# Task 2
try:
    num = int(input("Введите число: "))
    if num > 0:
        print("Число положительное!")
    else:
        print("Число не положительное!")
except ValueError:
    print("Ошибка! Вы ввели не число!")

# Task 3
try:
    num = int(input("Введите число: "))
    if num % 2 == 0:
        print("Число чётное")
    else:
        print("Число нечётное")
except ValueError:
    print("Ошибка! Вы ввели не число!")

# Task 4
try:
    num = int(input("Введите число: "))
    print("Чётное" if num % 2 == 0 else "Нечётное")
except ValueError:
    print("Ошибка! Вы ввели не число!")

# Task 5
try:
    num = int(input("Введите число: "))
    if num % 3 == 0:
        print("Число кратно 3")
    else:
        print("Число не кратно 3")
except ValueError:
    print("Ошибка! Вы ввели не число!")
