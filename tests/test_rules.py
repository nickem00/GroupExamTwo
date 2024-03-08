import unittest
from unittest.mock import patch
from oopython.src import tools
from oopython.src import rules


class TestRulesClass(unittest.TestCase):

    def test_init(self):
        r = rules.Rules()
        self.assertIsInstance(r.tools, tools.Tools)

    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    def test_show_rules(self, mock_enter_to_continue, mock_clear_screen,
                        mock_print):
        r = rules.Rules()
        r.show_rules()
        mock_print.assert_called_with('''Welcome to the PIG Dice Game!
        Here are the rules:
        1. The game is played by two players.
        A human player and a computer player.
        2. The game is turn-based. The human player goes first.
        3. The goal of the game is to reach 100 points.
        4. If a player rolls a 1, the player's turn ends and the player
        loses all points accumulated during the turn.
        5. If a player rolls a 2-6, the player can choose to roll again.
        6. If a player chooses to hold, the points accumulated during the
        turn are added to the player's total points.
        7. The computer player is set to easy difficulty by default.
        ''')
        mock_clear_screen.assert_called()
        mock_enter_to_continue.assert_called()
