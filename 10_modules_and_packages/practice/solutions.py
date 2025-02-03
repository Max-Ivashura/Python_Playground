import math
import random
from my_module import greet

# Task 1
print(math.sqrt(16))

# Task 2
num = random.randint(1, 10)
print("Рандомное число:", num)

# Task 3,4
print(greet())

# Task 5
try:
    import abcd
except Exception as e:
    print(e)
