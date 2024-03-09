import unittest
import tools
import rules
import settingsClass
import playerVsPlayer
import player
import developer
import histogram
import highscore
import intelligence
from unittest.mock import patch, MagicMock
from exceptions import (GameExitException, RolledAOneException)


class MockExitException(Exception):
    pass


class TestPlayerVsPlayerClass(unittest.TestCase):

    def test_init(self):
        game = playerVsPlayer.PlayerVsPlayer()
        self.assertIsNone(game.player_one)
        self.assertIsNone(game.player_two)
        self.assertIsInstance(game.tools, tools.Tools)
        self.assertEqual(game.difficulty, 1)
        self.assertIsInstance(game.settings, settingsClass.SettingsClass)
        self.assertIsInstance(game.all_rules, rules.Rules)
        self.assertIsInstance(game.intelligence, intelligence.Intelligence)
        self.assertIsInstance(game.developer, developer.Developer)
        self.assertIsInstance(game.histogram, histogram.Histogram)
        self.assertIsInstance(game.highscores, highscore.Highscore)
        self.assertEqual(game.main_menu_options, [
            '1. Start Game\n',
            '2. Show Rules\n'
            '3. Show Highscores\n',
            '4. Exit Game\n'
        ])
        self.assertEqual(game.game_menu_options, [
            '1. Roll\n',
            '2. Hold\n',
            '3. Show Rules\n',
            '4. Change Name\n',
            '5. Show Histogram\n',
            '6. Exit game (Points Reset)\n',
            '7. Developer Menu\n'
        ])

    # test of the game_starup method
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Player 1', 'Player 2', 4])
    @patch('tools.Tools.clear_screen')
    @patch('sys.exit', side_effect=MockExitException)
    def test_game_startup(self, mock_clear_screen, mock_input, mock_print,
                          mock_exit):
        game = playerVsPlayer.PlayerVsPlayer()
        with self.assertRaises(MockExitException):
            game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        self.assertEqual(game.player_one.name, 'Player 1')
        self.assertEqual(game.player_two.name, 'Player 2')

    # test of game_starup method with wrong input
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Player 1', 'Player 2',
                                          5, 'a', 4])
    @patch('tools.Tools.clear_screen')
    @patch('time.sleep')
    @patch('sys.exit', side_effect=MockExitException)
    def test_game_startup_wrong_input(self, mock_exit, mock_sleep,
                                      mock_clear_screen, mock_input,
                                      mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        with self.assertRaises(MockExitException):
            game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        self.assertEqual(game.player_one.name, 'Player 1')
        self.assertEqual(game.player_two.name, 'Player 2')

    # test of the start_game method
    @patch('builtins.print')
    @patch('playerVsPlayer.PlayerVsPlayer.start_round')
    @patch('tools.Tools.enter_to_continue')
    def test_start_game(self, mock_enter_to_continue, mock_start_round,
                        mock_print):
        mock_start_round.side_effect = [None, None, None, GameExitException]
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_two = player.Player('Player 2')
        game.start_game()

    # test of the start_round method
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['a', 1, 6])
    @patch('player.Player.roll_die', return_value=2)
    @patch('time.sleep')
    def test_start_round_option_one(self, mock_sleep, mock_roll_die,
                                    mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_two = player.Player('Player 2')
        with self.assertRaises(GameExitException):
            game.start_round(0, game.player_one)

    # test of the except RolledAOneException in start_round method
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[1, 6])
    @patch('time.sleep')
    def test_start_round_rolled_a_one(self, mock_sleep,
                                      mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_two = player.Player('Player 2')
        game.player_one.roll_die = MagicMock(side_effect=RolledAOneException)
        game.start_round(0, game.player_one)

    # test of option 2 in the start_round methods menu, which is hold
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[2, 6])
    @patch('time.sleep')
    def test_start_round_hold_winning(self, mock_sleep, mock_input,
                                      mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_one.total_score = 100
        game.player_one.hold = MagicMock()
        with self.assertRaises(GameExitException):
            game.start_round(0, game.player_one)
        self.assertEqual(game.player_one.total_score, 100)
        game.player_one.hold.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[2, 6])
    def test_start_round_hold_not_winning(self, mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_one.total_score = 0
        game.player_one.hold = MagicMock()
        game.print_points = MagicMock()
        game.start_round(0, game.player_one)
        self.assertEqual(game.player_one.total_score, 0)
        game.player_one.hold.assert_called()
        game.print_points.assert_called()

    # test of option 3 in the start_round methods menu, which is show rules
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[3, 6])
    @patch('tools.Tools.enter_to_continue')
    def test_start_round_show_rules(self, mock_enter_to_continue, mock_input,
                                    mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.all_rules.show_rules = MagicMock()
        with self.assertRaises(GameExitException):
            game.start_round(0, game.player_one)
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[4, 1, 'New_name', 6])
    @patch('tools.Tools.enter_to_continue')
    @patch('time.sleep')
    def test_change_name_player_one(self, mock_sleep,
                                    mock_enter_to_continue,
                                    mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_two = player.Player('Player 2')
        with self.assertRaises(GameExitException):
            game.start_round(0, game.player_one)
        self.assertEqual(game.player_one.name, 'New_name')
        self.assertEqual(game.player_two.name, 'Player 2')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[4, 'a', 2, 'New_name', 6])
    @patch('tools.Tools.enter_to_continue')
    @patch('time.sleep')
    def test_change_name_player_two(self, mock_sleep,
                                    mock_enter_to_continue,
                                    mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_two = player.Player('Player 2')
        with self.assertRaises(GameExitException):
            game.start_round(1, game.player_two)
        self.assertEqual(game.player_two.name, 'New_name')
        self.assertEqual(game.player_one.name, 'Player 1')
        mock_sleep.assert_called_with(2)

    def test_show_rules(self):
        game = playerVsPlayer.PlayerVsPlayer()
        game.all_rules.show_rules = MagicMock()
        game.show_rules()
        self.assertTrue(game.all_rules.show_rules.called)

    @patch('builtins.print')
    def test_print_points(self, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.player_two = player.Player('Player 2')
        game.print_points()
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[5, 6])
    def test_option_five_game_menu(self, mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.histogram.show_histogram = MagicMock()
        with self.assertRaises(GameExitException):
            game.start_round(0, game.player_one)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[7, 6])
    def test_option_six_game_menu(self, mock_input, mock_print):
        game = playerVsPlayer.PlayerVsPlayer()
        game.player_one = player.Player('Player 1')
        game.developer.developer_menu = MagicMock()
        with self.assertRaises(GameExitException):
            game.start_round(0, game.player_one)
        self.assertTrue(game.developer.developer_menu.called)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['player_one', 'player_two', 3, 4])
    @patch('sys.exit', side_effect=MockExitException)
    def test_option_three_main_menu(self, mock_input, mock_print, mock_exit):
        game = playerVsPlayer.PlayerVsPlayer()
        game.highscores.display_highscores = MagicMock()
        with self.assertRaises(MockExitException):
            game.game_startup()
        self.assertTrue(game.highscores.display_highscores.called)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['player_one', 'player_two', 2, 4])
    @patch('sys.exit', side_effect=MockExitException)
    def test_option_two_main_menu(self, mock_input, mock_print, mock_exit):
        game = playerVsPlayer.PlayerVsPlayer()
        game.all_rules.show_rules = MagicMock()
        with self.assertRaises(MockExitException):
            game.game_startup()
        self.assertTrue(game.all_rules.show_rules.called)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['player_one', 'player_two', 1, 4])
    @patch('sys.exit', side_effect=MockExitException)
    def test_start_game_main_menu(self, mock_input, mock_print, mock_exit):
        game = playerVsPlayer.PlayerVsPlayer()
        game.start_game = MagicMock()
        with self.assertRaises(MockExitException):
            game.game_startup()
        self.assertTrue(game.start_game.called)
