# 11_oop/main.py

# Пример 1: Создание класса
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} говорит: Гав!"


my_dog = Dog("Бобик")
print(my_dog.bark())


# Пример 2: Наследование
class Cat(Dog):
    def meow(self):
        return f"{self.name} говорит: Мяу!"


my_cat = Cat("Мурзик")
print(my_cat.meow())

# Пример 3: Ошибка из-за отсутствия self
# class Dog:
#     def __init__(name):
#         self.name = name  # Ошибка: NameError: name 'self' is not defined
