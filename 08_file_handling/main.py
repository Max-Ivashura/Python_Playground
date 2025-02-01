# 08_file_handling/main.py

# Пример 1: Запись в файл
with open("example.txt", "w") as file:
    file.write("Привет, мир!")

# Пример 2: Чтение из файла
with open("example.txt", "r") as file:
    content = file.read()
    print("Содержимое файла:", content)

# Пример 3: Ошибка из-за отсутствия файла
# with open("nonexistent.txt", "r") as file:
#     content = file.read()  # Ошибка: FileNotFoundError
