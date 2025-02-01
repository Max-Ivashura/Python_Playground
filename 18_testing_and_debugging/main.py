# 18_testing_and_debugging/main.py

# Пример 1: Использование unittest
import unittest


def add(a, b):
    return a + b


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()

# Пример 2: Ошибка из-за неправильного теста
# self.assertEqual(add(2, 3), 6)  # Ошибка: AssertionError
