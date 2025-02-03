import abc
import math


class Engine:
    def __init__(self, power, fuel_type):
        self.__power = power
        self.__fuel_type = fuel_type

    def set_power(self, new_power):
        self.__power = new_power

    def get_power(self):
        return self.__power

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def get_fuel_type(self):
        return self.__fuel_type

    def engine_info(self):
        return f"Мощность: {self.get_power()} л.с., Тип топлива: {self.get_fuel_type()}"

    def __str__(self):
        return self.engine_info()


class Car:
    def __init__(self, brand, model, year, engine: Engine):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__engine = engine
        self.__mileage = 0

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if not value < 0:
            self.__mileage = value
        else:
            print("Пробег не может быть отрицательным!")

    @staticmethod
    def is_vintage(year):
        return year > 25

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        self.__year = new_year

    def info(self):
        print(self)

    def __str__(self):
        return (f"Автомобиль: {self.get_brand()} {self.get_model()},"
                f" {self.get_year()} год выпуска, Двигатель: {self.__engine}")

    def __eq__(self, other):
        return (self.get_brand() == other.get_brand() and
                self.get_model() == other.get_model() and
                self.get_year() == other.get_year())


class ElectricalCar(Car):
    def __init__(self, brand, model, year, battery_capacity, engine: Engine):
        super().__init__(brand, model, year, engine)
        self.__battery_capacity = battery_capacity

    def set_battery_capacity(self, new_battery_capacity):
        self.__battery_capacity = new_battery_capacity

    def get_battery_capacity(self):
        return self.__battery_capacity

    def __str__(self):
        return (f"Автомобиль: {self.get_brand()} {self.get_model()},"
                f" {self.get_year()} год выпуска,"
                f" Ёмкость аккумулятора: {self.get_battery_capacity()} кВт·ч,"
                f" Двигатель: {self._Car__engine}")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: неопределенный звук?")

    def __str__(self):
        return f"Животное: {self.name}"


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: Гав!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Мяу!")


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"Прямоугольник: ширина = {self.__width}, высота = {self.__height}, площадь = {self.area()}"


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f"Круг: радиус = {self.__radius}, площадь = {self.area()}"


class HybridCar(ElectricalCar, Car):
    def __init__(self, fuel_type, brand, model, year, battery_capacity, engine: Engine):
        super().__init__(brand, model, year, battery_capacity, engine)
        self.__fuel_type = fuel_type

    def set_fuel_type(self, new_fuel_type):
        self.__fuel_type = new_fuel_type

    def get_fuel_type(self):
        return self.__fuel_type

    def __str__(self):
        return (f"Автомобиль: {self.get_brand()} {self.get_model()},"
                f" {self.get_year()} год выпуска,"
                f" Ёмкость аккумулятора: {self.get_battery_capacity()} кВт·ч,"
                f" Тип топлива: {self.get_fuel_type()},"
                f" Двигатель: {self._Car__engine}")


if __name__ == '__main__':
    engine = Engine(200, "бензин")
    car1 = Car("BMW", "F90", 2024, engine)
    car1.info()

    electric_engine = Engine(300, "электричество")
    car2 = ElectricalCar("Tesla", "Model S", 2023, 20000, electric_engine)
    car2.info()

    hybrid_engine = Engine(250, "гибрид")
    car3 = HybridCar("бензин", "Toyota", "Prius", 2022, 10000, hybrid_engine)
    car3.info()

    dog = Dog("Бобик")
    dog.speak()

    cat = Cat("Мурзик")
    cat.speak()

    rectangle = Rectangle(10, 20)
    print(rectangle)

    circle = Circle(5)
    print(circle)
