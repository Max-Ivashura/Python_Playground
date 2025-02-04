# Task 1
class MyIterator:
    def __init__(self):
        self.current = 1
        self.end = 5

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# Использование итератора
my_iter = MyIterator()
for number in my_iter:
    print(number)


# Task 2
def my_generator():
    for number in range(1, 6):
        yield number


# Использование генератора
for number in my_generator():
    print(number)


# Task 3
def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


# Использование генератора
gen = infinite_sequence()
for _ in range(10):  # Выведем первые 10 чисел
    print(next(gen))

# Task 4
my_list = [10, 20, 30, 40, 50]

# Создание итератора из списка
my_iter = iter(my_list)

# Обход списка с использованием итератора
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break


# Task 5
def even_numbers():
    num = 2
    while True:
        yield num
        num += 2


# Использование генератора
gen = even_numbers()
for _ in range(5):  # Выведем первые 5 чётных чисел
    print(next(gen))

