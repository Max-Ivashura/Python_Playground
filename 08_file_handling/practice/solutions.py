# Task 1
with open("example.txt", 'w') as file:
    file.write("Привет, мир!")

# Task 3
with open("example.txt", 'a') as file:
    file.write("\nЕщё одна строка")

# Task 2
with open("example.txt", 'r') as file:
    data = file.read()
    print("Файл содержит:", data)

# Task 4
with open("numbers.txt", 'w') as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

# Task 5
sum = 0
with open("numbers.txt", 'r') as file:
    data = file.read().split()  # Разделяем строку по пробелам или переводам строк
    for number in data:
        sum += int(number)
print(sum)