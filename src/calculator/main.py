#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main for using the calculator."""

import calculator


def main():
    """Use the calculator."""
    calc = calculator.Calculator()
    print(f"The sum is = {calc.sum()}")

    ret = calc.add(5, 9)
    print(f"The return value was: {ret}")
    print(f"The sum is = {calc.sum()}")

    ret = calc.subtract(20, 10)
    print(f"The return value was: {ret}")
    print(f"The sum is = {calc.sum()}")

    ret = calc.multiply(2, 2)
    print(f"The return value was: {ret}")
    print(f"The sum is = {calc.sum()}")

    ret = calc.division(33, 3)
    print(f"The return value was: {ret}")
    print(f"The sum is = {calc.sum()}")

    try:
        ret = calc.division(1, 0)
        print(f"The return value was: {ret}")
        print(f"The sum is = {calc.sum()}")
    except ZeroDivisionError:
        print("Failed division due to division by zero.")
        print(f"The sum is = {calc.sum()}")

    ret = calc.division1(1, 0)
    print(f"The return value was: {ret}")
    print(f"The sum is = {calc.sum()}")

    ret = calc.random(1, 6)
    print(f"The return value was: {ret}")
    print(f"The sum is = {calc.sum()}")

    try:
        ret = calc.random(1, 1)
        print(f"The return value was: {ret}")
        print(f"The sum is = {calc.sum()}")
    except ValueError:
        print("Failed generating random number.")
        print(f"The sum is = {calc.sum()}")


if __name__ == "__main__":
    # Call the main function.
    main()
