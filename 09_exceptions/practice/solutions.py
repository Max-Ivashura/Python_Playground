def checker(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(f"Произошла ошибка: {ex}")
            return None

    return wrapper


@checker
def get_number():
    number = int(input("Введите число для возведения в квадрат: "))
    return number ** 2


@checker
def get_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        print(data)


@checker
def division(n1, n2):
    return n1 / n2


class MyException(Exception):
    pass


@checker
def exception_test():
    raise MyException("This is test ex?")


if __name__ == '__main__':
    # Task 1
    result = get_number()
    if result is not None:
        print("Результат:", result)

    # Task 2
    get_file("nonexistent.txt")

    # Task 3
    division(5, 0)

    # Task 4
    exception_test()

    # Task 5
    file = None
    try:
        file = open("tasks.md", "r")
        data = file.read()
        print(data)
    except Exception as ex:
        print("Ошибка:", ex)
    finally:
        file.close()
