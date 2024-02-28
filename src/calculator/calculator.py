#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a class for a calculator."""

import random


class Calculator:
    """Example of calculator class."""

    def __init__(self):
        """Initiate the calculator."""
        random.seed()
        self.total = 0

    def add(self, a, b):
        """Addition of two numbers."""
        self.total += a + b
        return a + b

    def subtract(self, a, b):
        """Subtraction of two numbers."""
        self.total += a - b
        return a - b

    def multiply(self, a, b):
        """Multiplication of two numbers."""
        self.total += a * b
        return a * b

    def division(self, a, b):
        """Division of two numbers."""
        self.total += a / b
        return a / b

    def division1(self, a, b):
        """Division of two numbers, disallow division by 0."""
        if b == 0:
            return "Division by zero is not allowed!"
        self.total += a / b
        return a / b

    def random(self, a, b):
        """Randomize a number between."""
        num = random.randrange(a, b)
        self.total += num
        return num

    def sum(self):
        """Return the sum."""
        return self.total
