import unittest
import dice


class test_dice(unittest.TestCase):
    """Test the Dice class."""

    def test_init_(self):
        """Tests the constructor for the Dice class."""
        d = dice.Dice()
        self.assertIsInstance(d, dice.Dice)

    def test_roll(self):
        """Tests the roll method of the Dice class."""
        d = dice.Dice()
        result = d.roll()
        self.assertTrue(1 <= result <= 6)
