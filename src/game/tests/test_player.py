import unittest
from player import Player
from dice import Dice
from tools import Tools
from exceptions import RolledAOneException
from unittest.mock import MagicMock, patch


class TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def test_player_constructor(self):
        """Tests the constructor for the Player class."""
        player_name = "Test"
        player = Player(player_name)

        self.assertEqual(player.name, "Test")
        self.assertEqual(player.total_score, 0)
        self.assertEqual(player.round_score, 0)
        self.assertIsInstance(player.die, Dice)
        self.assertIsInstance(player.tools, Tools)

    @patch("dice.Dice.roll")
    def test_roll_die_one(self, mock_roll):
        """
        Tests the roll_die method of the Player class when the die
        rolls a one."""
        player = Player("Test")
        mock_roll.return_value = 1
        histogram = MagicMock()
        with self.assertRaises(RolledAOneException):
            player.roll_die(histogram)
        self.assertEqual(player.round_score, 0)
        histogram.add_to_histogram.assert_called_with(1)

    @patch("dice.Dice.roll")
    def test_roll_die_not_one(self, mock_roll):
        """
        Tests the roll_die method of the Player class when the die
        does not roll a one.
        """
        player = Player("Test")
        mock_roll.return_value = 2
        histogram = MagicMock()
        roll = player.roll_die(histogram)
        self.assertEqual(roll, 2)
        self.assertEqual(player.round_score, 2)
        histogram.add_to_histogram.assert_called_with(2)

    def test_hold(self):
        """Tests the hold method of the Player class."""
        player = Player("Test")
        player.round_score = 5
        player.rolls = [3, 2]
        player.highscores = MagicMock()
        player.hold(player.highscores)
        self.assertEqual(player.total_score, 5)
        self.assertEqual(player.round_score, 0)
        player.highscores.save_new_highscore.assert_called_with("Test", 5)

    def test_is_winning(self):
        """Tests the is_winning method of the Player class."""
        player = Player("Test")
        player.total_score = 100
        winning_score = 100
        self.assertTrue(player.is_winning(winning_score))
        winning_score = 101
        self.assertFalse(player.is_winning(winning_score))

    def test_set_name(self):
        """Tests the set_name method of the Player class."""
        player = Player("Test")
        player.set_name("New Name")
        self.assertEqual(player.name, "New Name")
