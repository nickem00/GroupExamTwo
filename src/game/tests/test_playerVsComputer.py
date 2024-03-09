# unittest of the playerVsComputer module
import unittest
from unittest.mock import patch, MagicMock
import playerVsComputer
import tools
import settingsClass
import rules
import intelligence
import developer
import histogram
import highscore
import player
from exceptions import (GameExitException, RolledAOneException,
                        ComputerWonException)


class MockExitException(Exception):
    pass


class TestPlayerVsComputerClass(unittest.TestCase):

    def test_init(self):
        game = playerVsComputer.PlayerVsComputer()
        self.assertIsInstance(game.computer_player,
                              intelligence.Intelligence)
        self.assertIsNone(game.human_player)
        self.assertIsInstance(game.tools, tools.Tools)
        self.assertEqual(game.difficulty, 1)
        self.assertIsInstance(game.settings, settingsClass.SettingsClass)
        self.assertIsInstance(game.all_rules, rules.Rules)
        self.assertIsInstance(game.intelligence, intelligence.Intelligence)
        self.assertIsInstance(game.developer, developer.Developer)
        self.assertIsInstance(game.histogram, histogram.Histogram)
        self.assertIsInstance(game.highscores, highscore.Highscore)

    '''
    Unit tests of the main menu options of the game_startup method
    of the PlayerVsComputer class.
    '''

    @patch('builtins.input', side_effect=['test', '1', '5'])
    @patch('sys.exit', side_effect=MockExitException)
    @patch('tools.Tools.clear_screen')
    @patch('builtins.print')
    @patch('playerVsComputer.PlayerVsComputer.start_game')
    def test_option_one(self, mock_start_game, mock_print,
                        mock_clear_screen,
                        mock_input, mock_exit):
        game = playerVsComputer.PlayerVsComputer()
        with self.assertRaises(MockExitException):
            game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_start_game.assert_called()

    @patch('builtins.input', side_effect=['test', '2', '5'])
    @patch('sys.exit', side_effect=MockExitException)
    @patch('tools.Tools.clear_screen')
    @patch('builtins.print')
    @patch('rules.Rules.show_rules')
    def test_option_two(self, mock_show_rules, mock_print,
                        mock_clear_screen,
                        mock_input, mock_exit):
        game = playerVsComputer.PlayerVsComputer()
        with self.assertRaises(MockExitException):
            game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_show_rules.assert_called()

    @patch('builtins.input', side_effect=['test', '3', 'new_name', '5'])
    @patch('sys.exit', side_effect=MockExitException)
    @patch('tools.Tools.clear_screen')
    @patch('builtins.print')
    def test_option_three(self, mock_print, mock_clear_screen,
                          mock_input, mock_exit):
        game = playerVsComputer.PlayerVsComputer()
        with self.assertRaises(MockExitException):
            game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        self.assertEqual(game.human_player.name, 'new_name')

    @patch('builtins.input', side_effect=['test', '4', '5'])
    @patch('sys.exit', side_effect=MockExitException)
    @patch('tools.Tools.clear_screen')
    @patch('builtins.print')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.display_highscores')
    def test_option_four(self, mock_display_highscores, mock_enter_to_continue,
                         mock_print, mock_clear_screen,
                         mock_input, mock_exit):
        game = playerVsComputer.PlayerVsComputer()
        with self.assertRaises(MockExitException):
            game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_display_highscores.assert_called()

    @patch('builtins.input', side_effect=['test', '6', '5'])
    @patch('sys.exit', side_effect=MockExitException)
    @patch('tools.Tools.clear_screen')
    @patch('builtins.print')
    def test_invalid_option(self, mock_print, mock_clear_screen,
                            mock_input, mock_exit):
        game = playerVsComputer.PlayerVsComputer()
        with self.assertRaises(MockExitException):
            with self.assertRaises(ValueError):
                game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()

    @patch('builtins.input', side_effect=['test', 'a', '5'])
    @patch('sys.exit', side_effect=MockExitException)
    @patch('tools.Tools.clear_screen')
    @patch('builtins.print')
    @patch('time.sleep')
    def test_invalid_option_letter(self, mock_sleep, mock_print,
                                   mock_clear_screen, mock_input, mock_exit):
        game = playerVsComputer.PlayerVsComputer()
        with self.assertRaises(MockExitException):
            with self.assertRaises(ValueError):
                game.game_startup()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_sleep.assert_called()

    '''
    End of unit tests of the main menu options of the game_startup method.
    '''

    @patch('builtins.print')
    def test_print_main_menu(self, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = MagicMock()
        main_menu_options = {'1': 'Option 1', '2': 'Option 2'}
        game.print_main_menu(main_menu_options)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_print_game_menu(self, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = MagicMock()
        game_menu_options = {'1': 'Option 1', '2': 'Option 2'}
        game.print_game_menu(game_menu_options)
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '2', '4', '5'])
    @patch('tools.Tools.enter_to_continue')
    @patch('sys.exit', side_effect=MockExitException)
    def test_start_game(self, mock_exit, mock_enter_to_continue,
                        mock_input, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.start_game()
        mock_print.assert_called()

    '''
    Unit tests of the human_players_turn method of the PlayerVsComputer class.
    '''

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '4'])
    @patch('time.sleep')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    def test_human_players_turn(self, mock_enter_to_continue,
                                mock_clear_screen, mock_sleep,
                                mock_input, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock(side_effect=GameExitException)),
            '2': ('Hold', MagicMock()),
            '3': ('Change Difficulty', MagicMock()),
            '4': ('Exit game (Points reset)', MagicMock()),
            '5': ('Show Histogram', MagicMock()),
            '6': ('Dev-Options', MagicMock())
        }
        with self.assertRaises(GameExitException):
            game.human_players_turn(0, game_menu_options)

        mock_clear_screen.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['a', '4'])
    @patch('time.sleep')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    def test_human_players_turn_letter(self, mock_enter_to_continue,
                                       mock_clear_screen, mock_sleep,
                                       mock_input, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock(side_effect=GameExitException)),
            '2': ('Hold', MagicMock()),
            '3': ('Change Difficulty', MagicMock()),
            '4': ('Exit game (Points reset)', MagicMock()),
            '5': ('Show Histogram', MagicMock()),
            '6': ('Dev-Options', MagicMock())
        }
        with self.assertRaises(GameExitException):
            game.human_players_turn(0, game_menu_options)

        mock_clear_screen.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '5'])
    def test_human_players_turn_rolled_a_one(self, mock_input,
                                             mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock(side_effect=RolledAOneException)),
            '2': ('Hold', MagicMock())
        }
        game.human_players_turn(0, game_menu_options)

    # a test of the human_players_turn method when he chooses option two
    # (hold).
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '5'])
    def test_human_players_turn_hold_not_winning(self, mock_input, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock()),
            '2': ('Hold', MagicMock())
        }
        game.human_players_turn(0, game_menu_options)

    # a test of the human_players_turn method when he chooses option two
    # (hold) and is winning.
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '5'])
    def test_human_players_turn_hold_winning(self, mock_input, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()
        game.human_player.total_score = 100

        game_menu_options = {
            '1': ('Roll die', MagicMock()),
            '2': ('Hold', MagicMock())
        }
        game.human_players_turn(0, game_menu_options)

    # a test of the human_players_turn method when he chooses option five
    # (show histogram). mocking histogram.show_histogram method.
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['5', '4'])
    def test_human_players_turn_show_histogram(self, mock_input, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock()),
            '2': ('Hold', MagicMock()),
            '3': ('Change Difficulty', MagicMock()),
            '4': ('Exit game (Points reset)', MagicMock()),
            '5': ('Show Histogram', game.histogram.show_histogram),
            '6': ('Dev-Options', MagicMock())
        }
        with self.assertRaises(GameExitException):
            game.human_players_turn(0, game_menu_options)
        game.histogram.show_histogram.assert_called()

    # a test of the human_players_turn method when he chooses option six
    # (developer options). mocking developer.developer_menu method.
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['6', '4'])
    def test_human_players_turn_developer_options(self, mock_input,
                                                  mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()
        game.developer = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock()),
            '2': ('Hold', MagicMock()),
            '3': ('Change Difficulty', MagicMock()),
            '4': ('Exit game (Points reset)', MagicMock()),
            '5': ('Show Histogram', MagicMock()),
            '6': ('Dev-Options', game.developer.developer_menu)
        }
        with self.assertRaises(GameExitException):
            game.human_players_turn(0, game_menu_options)
        game.developer.developer_menu.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '4'])
    def test_human_players_turn_else(self, mock_input,
                                     mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()
        game.change_difficulty = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock()),
            '2': ('Hold', MagicMock()),
            '3': ('Change Difficulty', game.change_difficulty()),
            '4': ('Exit game (Points reset)', MagicMock()),
            '5': ('Show Histogram', MagicMock()),
            '6': ('Dev-Options', MagicMock())
        }
        with self.assertRaises(GameExitException):
            game.human_players_turn(0, game_menu_options)
        game.change_difficulty.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['9', '4'])
    def test_human_players_turn_invalid(self, mock_input,
                                        mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.human_player = player.Player('test')
        game.histogram = MagicMock()
        game.highscores = MagicMock()

        game_menu_options = {
            '1': ('Roll die', MagicMock()),
            '2': ('Hold', MagicMock()),
            '3': ('Change Difficulty', MagicMock()),
            '4': ('Exit game (Points reset)', MagicMock()),
            '5': ('Show Histogram', MagicMock()),
            '6': ('Dev-Options', MagicMock())
        }
        with self.assertRaises(GameExitException):
            game.human_players_turn(0, game_menu_options)

    '''
    End of unit tests of the human_players_turn method.
    '''

    @patch('builtins.print')
    @patch('intelligence.Intelligence.start_round')
    @patch('tools.Tools.enter_to_continue')
    def test_computer_players_turn(self, mock_enter_to_continue,
                                   mock_start_round, mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.computer_player = intelligence.Intelligence()
        game.computer_player.total_score = 100
        with self.assertRaises(ComputerWonException):
            game.computer_players_turn()
        mock_start_round.assert_called()

    # test of the change_difficulty method of the PlayerVsComputer class.
    @patch('builtins.print')
    @patch('settingsClass.SettingsClass.change_difficulty', return_value=1)
    def test_change_difficulty_same(self, mock_change_difficulty,
                                    mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.change_difficulty()
        mock_change_difficulty.assert_called()
        mock_print.assert_called_with('You selected the same difficulty.')

    @patch('builtins.print')
    @patch('settingsClass.SettingsClass.change_difficulty', return_value=2)
    def test_change_difficulty(self, mock_change_difficulty,
                               mock_print):
        game = playerVsComputer.PlayerVsComputer()
        game.change_difficulty()
        mock_change_difficulty.assert_called()
        mock_print.assert_called_with('You selected a new difficulty!')
