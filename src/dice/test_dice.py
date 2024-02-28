#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import dice


class TestDiceClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.faces
        exp = 6
        self.assertEqual(res, exp)

    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= die.faces
        self.assertTrue(exp)

    def test_set_faces(self):
        """Tests the ability to set costum number of faces on dice."""
        die = dice.Dice()

        die.set_faces(6)
        self.assertTrue(die.faces == 6)

    def test_get_rolls_made(self):
        """Gets the number of rolls made."""
        die = dice.Dice()
        die.get_rolls_made()

    def test_get_sum_rolls(self):
        """Gets the sum of alla rolls made."""
        die = dice.Dice()
        die.get_sum_rolls()


if __name__ == "__main__":
    unittest.main()
