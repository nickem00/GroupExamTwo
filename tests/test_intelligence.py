import unittest
from oopython.src import intelligence
from oopython.src import dice
from oopython.src.exceptions import RolledAOneException
from unittest.mock import MagicMock
from oopython.src import tools


class TestIntelligenceClass(unittest.TestCase):

    def test_init(self):
        i = intelligence.Intelligence()
        self.assertEqual(i.name, "Computer")
        self.assertEqual(i.difficulty, 0)
        self.assertEqual(i.total_score, 0)
        self.assertEqual(i.round_score, 0)
        self.assertEqual(i.roll_until_hold, 0)
        self.assertIsInstance(i.die, dice.Dice)
        self.assertEqual(i.rolls, [])
        self.assertIsInstance(i.tools, tools.Tools)

    def test_start_round(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()

        i.easy = MagicMock()
        i.start_round(1, mock_histogram)
        i.easy.assert_called_with(mock_histogram)

        i.medium = MagicMock()
        i.start_round(2, mock_histogram)
        i.medium.assert_called_with(mock_histogram)

        i.hard = MagicMock()
        i.start_round(3, mock_histogram)
        i.hard.assert_called_with(mock_histogram)

    def test_hold(self):
        i = intelligence.Intelligence()
        i.round_score = 5
        i.rolls = [1, 2, 3]
        i.hold()
        self.assertEqual(i.total_score, 5)
        self.assertEqual(i.round_score, 0)
        self.assertEqual(i.rolls, [])

    def test_easy(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()
        i.roll_die = MagicMock()
        i.roll_until_hold = 2
        i.easy(mock_histogram)
        self.assertEqual(i.roll_die.call_count, 2)

    def test_medium(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()
        i.roll_die = MagicMock()
        i.roll_until_hold = 3
        i.medium(mock_histogram)
        self.assertEqual(i.roll_die.call_count, 3)

    def test_hard(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()
        i.roll_die = MagicMock()
        i.roll_until_hold = 4
        i.hard(mock_histogram)
        self.assertEqual(i.roll_die.call_count, 4)

    def test_roll_die_one(self):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=1)
        histogram = MagicMock()

        with self.assertRaises(RolledAOneException):
            i.roll_die(histogram)

        self.assertEqual(i.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    def test_roll_die_not_one(self):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=2)
        histogram = MagicMock()

        roll = i.roll_die(histogram)

        self.assertEqual(roll, 2)
        self.assertEqual(i.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

    def test_is_winning(self):
        i = intelligence.Intelligence()
        i.total_score = 100
        self.assertTrue(i.is_winning(100))
        i.total_score = 99
        self.assertFalse(i.is_winning(100))
