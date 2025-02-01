# 14_iterators_and_generators/main.py

# Пример 1: Итератор
my_list = [1, 2, 3]
my_iter = iter(my_list)
print("Элементы итератора:")
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# Пример 2: Генератор
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print("Элементы генератора:")
for value in gen:
    print(value)

# Пример 3: Ошибка из-за исчерпания итератора
# print(next(my_iter))  # Ошибка: StopIteration
