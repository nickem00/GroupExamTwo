import unittest
from oopython.src import player
from oopython.src import dice
from oopython.src.exceptions import RolledAOneException
from unittest.mock import MagicMock


class TestPlayerClass(unittest.TestCase):

    def test_init(self):
        p = player.Player('Test')
        self.assertEqual(p.name, 'Test')
        self.assertEqual(p.total_score, 0)
        self.assertEqual(p.round_score, 0)
        self.assertIsInstance(p.die, dice.Dice)

    def test_roll_die_one(self):
        p = player.Player('Test')

        '''
        Ersätter roll metoden som finns i dice klassen, som finns i
        player klassen, med en mockad funktion, som returnerar 1.
        '''
        p.die.roll = MagicMock(return_value=1)
        histogram = MagicMock()

        with self.assertRaises(RolledAOneException):
            p.roll_die(histogram)

        self.assertEqual(p.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    def test_roll_die_not_one(self):
        p = player.Player('Test')
        p.die.roll = MagicMock(return_value=2)
        histogram = MagicMock()

        roll = p.roll_die(histogram)

        self.assertEqual(roll, 2)
        self.assertEqual(p.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

    def test_hold(self):
        p = player.Player('Test')
        p.round_score = 5
        p.hold()
        self.assertEqual(p.total_score, 5)
        self.assertEqual(p.round_score, 0)

    def test_is_winning(self):
        p = player.Player('Test')
        p.total_score = 100
        self.assertTrue(p.is_winning(100))
        p.total_score = 99
        self.assertFalse(p.is_winning(100))
