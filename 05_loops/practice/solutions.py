# Task 1
print("Task 1")
for i in range(1, 6):
    print(i)

# Task 2
print("Task 2")
x = 1
while x < 11:
    print(x)
    x += 1

# Task 3
print("Task 3")
for i in range(1, 11, 2):
    print(i)

# Task 4
print("Task 4")
x = 0
while x != 5:
    try:
        x = int(input("Введите число(5 для выхода):"))
    except ValueError:
        print("Введено не число!")

# Task 5
print("Task 5")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
