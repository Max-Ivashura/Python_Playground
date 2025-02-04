# Task 1
def messages(func):
    def wrapper():
        print("Начало функции!")
        func()
        print("Конец функции!")

    return wrapper


# Task 2
def repeat_3(func):
    def wrapper():
        for _ in range(3):
            func()

    return wrapper


# Task 3
import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        # Засекаем время начала выполнения
        start_time = time.time()

        # Вызываем исходную функцию
        result = func(*args, **kwargs)

        # Засекаем время окончания выполнения
        end_time = time.time()

        # Вычисляем время выполнения
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} секунд.")

        # Возвращаем результат исходной функции
        return result

    return wrapper


def cache_decorator(func):
    # Словарь для хранения кэшированных результатов
    cache = {}

    def wrapper(*args):
        # Если результат уже есть в кэше, возвращаем его
        if args in cache:
            print(f"Результат из кэша для аргументов {args}: {cache[args]}")
            return cache[args]

        # Иначе вычисляем результат и сохраняем его в кэше
        result = func(*args)
        cache[args] = result
        print(f"Результат вычислен для аргументов {args}: {result}")
        return result

    return wrapper


def numbers_only_decorator(func):
    def wrapper(*args):
        # Проверяем, что все аргументы — числа
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Аргумент {arg} не является числом!")

        # Если все аргументы — числа, вызываем функцию
        return func(*args)

    return wrapper


@timer_decorator
@messages
@repeat_3
def test_message():
    print("Моя тестовая функция")


if __name__ == '__main__':
    test_message()
