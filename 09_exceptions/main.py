# 09_exceptions/main.py

# Пример 1: Обработка исключений
try:
    x = int(input("Введите число: "))
    print("Вы ввели:", x)
except ValueError:
    print("Ошибка: вы ввели не число!")

# Пример 2: Блок finally
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()  # Файл будет закрыт, даже если возникнет ошибка


# Пример 3: Создание собственного исключения
class MyError(Exception):
    pass


try:
    raise MyError("Что-то пошло не так!")
except MyError as e:
    print("Поймано исключение:", e)
