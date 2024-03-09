# Test of the intelligence class.
import unittest
from unittest.mock import MagicMock, patch
import intelligence
import dice
import tools
from exceptions import RolledAOneException


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

    @patch('intelligence.Intelligence.easy')
    @patch('intelligence.Intelligence.medium')
    @patch('intelligence.Intelligence.hard')
    def test_start_round(self, mock_hard, mock_medium, mock_easy):
        i = intelligence.Intelligence()
        histogram = MagicMock()
        i.start_round(1, histogram)
        mock_easy.assert_called_with(histogram)

        i.start_round(2, histogram)
        mock_medium.assert_called_with(histogram)

        i.start_round(3, histogram)
        mock_hard.assert_called_with(histogram)

    @patch('builtins.print')
    def test_start_round_error(self, mock_print):
        i = intelligence.Intelligence()
        histogram = MagicMock()
        i.start_round(4, histogram)
        mock_print.assert_called_with('Error: Difficulty not set')

    @patch('intelligence.random.randint', return_value=1)
    def test_easy_one(self, mock_randint):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=1)
        histogram = MagicMock()
        i.easy(histogram)
        self.assertEqual(i.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    @patch('intelligence.random.randint', return_value=1)
    def test_easy_not_one(self, mock_randint):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=2)
        histogram = MagicMock()
        i.hold = MagicMock()
        i.easy(histogram)
        self.assertEqual(i.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

    @patch('intelligence.random.randint', return_value=1)
    def test_medium_one(self, mock_randint):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=1)
        histogram = MagicMock()
        i.medium(histogram)
        self.assertEqual(i.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    @patch('intelligence.random.randint', return_value=1)
    def test_medium_not_one(self, mock_randint):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=2)
        histogram = MagicMock()
        i.hold = MagicMock()
        i.medium(histogram)
        self.assertEqual(i.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

    @patch('intelligence.random.randint', return_value=1)
    def test_hard_one(self, mock_randint):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=1)
        histogram = MagicMock()
        i.hard(histogram)
        self.assertEqual(i.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    @patch('intelligence.random.randint', return_value=1)
    def test_hard_not_one(self, mock_randint):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=2)
        histogram = MagicMock()
        i.hold = MagicMock()
        i.hard(histogram)
        self.assertEqual(i.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

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
        i.roll_die(histogram)
        self.assertEqual(i.round_score, 2)
        self.assertEqual(i.rolls, [2])
        histogram.add_to_histogram.assert_called_with(2)

    def test_is_winning(self):
        i = intelligence.Intelligence()
        winning_score = 100
        i.total_score = 100
        self.assertTrue(i.is_winning(winning_score))

        i.total_score = 99
        self.assertFalse(i.is_winning(winning_score))

    @patch('builtins.print')
    def test_hold(self, mock_print):
        i = intelligence.Intelligence()
        i.round_score = 5
        i.hold()
        self.assertEqual(i.total_score, 5)
        self.assertEqual(i.round_score, 0)
        mock_print.assert_called()
