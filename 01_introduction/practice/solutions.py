# Task 1
print("Привет, мир!")

# Task 2
name = "Max"
print(f"Привет, {name}!")

# Task 3
try:
    age = int(input("Введите свой возраст: "))
    print(f"Тебе {age} лет.")
except ValueError:
    print("Ошибка: вы ввели не число!")

# Task 4
x = 10
if x > 5:
    print("x больше 5")

# Task 5
for i in range(1, 6):
    print(i)
