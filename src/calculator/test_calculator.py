#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import calculator


class TestCalculatorClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its default properties."""
        calc = calculator.Calculator()
        self.assertIsInstance(calc, calculator.Calculator)

        res = calc.sum()
        exp = 0
        self.assertEqual(res, exp)

    def test_addition(self):
        """Perform addition."""
        calc = calculator.Calculator()

        res = calc.add(1, 1)
        exp = 2
        self.assertEqual(res, exp)

        res = calc.sum()
        exp = 2
        self.assertEqual(res, exp)

    def test_subtraction(self):
        """Perform subtraction."""
        calc = calculator.Calculator()

        res = calc.subtract(4, 2)
        exp = 2
        self.assertEqual(res, exp)

        res = calc.sum()
        exp = 2
        self.assertEqual(res, exp)

    def test_multiply(self):
        """Perform multiplication."""
        calc = calculator.Calculator()

        res = calc.multiply(2, 2)
        exp = 4
        self.assertEqual(res, exp)

        res = calc.sum()
        exp = 4
        self.assertEqual(res, exp)

    def test_division(self):
        """Perform division."""
        calc = calculator.Calculator()

        res = calc.division(2, 2)
        exp = 1
        self.assertEqual(res, exp)

        res = calc.sum()
        exp = 1
        self.assertEqual(res, exp)

    def test_division1(self):
        """Perform division with division1."""
        calc = calculator.Calculator()

        res = calc.division1(2, 2)
        exp = 1
        self.assertEqual(res, exp)

        res = calc.sum()
        exp = 1
        self.assertEqual(res, exp)

    def test_division_by_zero_raise_exception(self):
        """Perform division by zero, raise exception."""
        calc = calculator.Calculator()

        with self.assertRaises(ZeroDivisionError):
            calc.division(2, 0)

        res = calc.sum()
        exp = 0
        self.assertEqual(res, exp)

    def test_division_by_zero_get_error_message(self):
        """Perform division by zero, get error message."""
        calc = calculator.Calculator()

        res = calc.division1(2, 0)
        exp = "Division by zero"
        self.assertIn(exp, res)

    def test_random(self):
        """Perform random."""
        calc = calculator.Calculator()

        res = calc.random(1, 6)
        exp = 1 <= res <= 6
        self.assertTrue(exp)

        res = calc.sum()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_random_raise_value_error(self):
        """Perform random with bad values to raise ValueError."""
        calc = calculator.Calculator()

        with self.assertRaises(ValueError):
            calc.random(1, 1)

        res = calc.sum()
        exp = 0
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
