import unittest
from oopython.src import intelligence
from oopython.src import dice
from oopython.src.exceptions import RolledAOneException
from unittest.mock import MagicMock
from oopython.src import tools


class TestIntelligenceClass(unittest.TestCase):

    '''
    Test the constructor of the Intelligence class and its attributes.
    '''
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

    '''
    Test the start_round method of the Intelligence class.
    It tests if the correct difficulty method is called based on the
    difficulty parameter. It uses a mock histogram to test the method.
    '''
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

    '''
    Test the hold method of the Intelligence class. It tests if the round
    score is added to the total score and if the round score is set to 0.
    The rolls list is also tested to be set to an empty list.
    '''
    def test_hold(self):
        i = intelligence.Intelligence()
        i.round_score = 5
        i.rolls = [1, 2, 3]
        i.hold()
        self.assertEqual(i.total_score, 5)
        self.assertEqual(i.round_score, 0)
        self.assertEqual(i.rolls, [])

    '''
    Test the easy method of the Intelligence class. It tests if the roll_die
    method is called the correct amount of times based on the roll_until_hold
    attribute.
    '''
    def test_easy(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()
        i.roll_die = MagicMock()
        i.roll_until_hold = 2
        i.easy(mock_histogram)
        self.assertEqual(i.roll_die.call_count, 2)

    '''
    The same test as above, but for the medium method.
    '''
    def test_medium(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()
        i.roll_die = MagicMock()
        i.roll_until_hold = 3
        i.medium(mock_histogram)
        self.assertEqual(i.roll_die.call_count, 3)

    '''
    The same test as above, but for the hard method.
    '''
    def test_hard(self):
        i = intelligence.Intelligence()
        mock_histogram = MagicMock()
        i.roll_die = MagicMock()
        i.roll_until_hold = 4
        i.hard(mock_histogram)
        self.assertEqual(i.roll_die.call_count, 4)

    '''
    Test the roll_die method of the Intelligence class when the roll is 1.
    It tests if the round score is set to 0 and if a RolledAOneException
    is raised. It also tests if the roll is added to the histogram.
    '''
    def test_roll_die_one(self):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=1)
        histogram = MagicMock()

        with self.assertRaises(RolledAOneException):
            i.roll_die(histogram)

        self.assertEqual(i.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    '''
    Test the roll_die method of the Intelligence class when the roll is not 1.
    It tests if the round score is set to the roll and if the roll is added
    to the histogram.
    '''
    def test_roll_die_not_one(self):
        i = intelligence.Intelligence()
        i.die.roll = MagicMock(return_value=2)
        histogram = MagicMock()

        roll = i.roll_die(histogram)

        self.assertEqual(roll, 2)
        self.assertEqual(i.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

    '''
    Test the is_winning method of the Intelligence class. It tests if the
    method returns True if the total score is equal to the winning score,
    and if the method returns False if the total score is less than the
    winning score.
    '''
    def test_is_winning(self):
        i = intelligence.Intelligence()
        i.total_score = 100
        self.assertTrue(i.is_winning(100))
        i.total_score = 99
        self.assertFalse(i.is_winning(100))
