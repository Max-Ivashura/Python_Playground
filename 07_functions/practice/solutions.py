# Task 1
def greet(name):
    return f"Привет, {name}!"


print(greet("Max"))


# Task 2
def add(a, b):
    return a + b


print(add(5, 8))


# Task 3
def is_even(number):
    return number % 2 == 0


print(is_even(4))


# Task 4
def square(a):
    return a ** 2


print(square(3))


# Task 5
def factorial(number):
    total = 1
    for i in range(2, number + 1):
        total *= i
    return total


print(factorial(10))
