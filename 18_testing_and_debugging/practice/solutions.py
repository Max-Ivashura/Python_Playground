import unittest
from my_module import *


# Тесты
class TestFunctions(unittest.TestCase):

    # Тесты для add
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -5), -6)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

    # Тесты для is_even
    def test_is_even_number(self):
        self.assertTrue(is_even(4))

    def test_is_odd_number(self):
        self.assertFalse(is_even(7))

    def test_is_even_zero(self):
        self.assertTrue(is_even(0))

    # Тесты для factorial
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_small_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    # Тесты для greet
    def test_greet_name(self):
        self.assertEqual(greet("Анна"), "Привет, Анна!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Привет, !")

    # Тесты для divide
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
