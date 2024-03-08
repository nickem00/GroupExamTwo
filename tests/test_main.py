import unittest
from unittest.mock import patch
from oopython.src import main


class TestMainClass(unittest.TestCase):

    @patch('oopython.src.tools.Tools.clear_screen')
    @patch('oopython.src.main.playerVsComputer.PlayerVsComputer.game_startup')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1'])
    def test_option_one(self, mock_input, mock_print, mock_clear_screen,
                        mock_game_startup):
        main.main()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_input.assert_called()

    @patch('oopython.src.tools.Tools.clear_screen')
    @patch('oopython.src.main.playerVsPlayer.PlayerVsPlayer.game_startup')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2'])
    def test_option_two(self, mock_input, mock_print, mock_clear_screen,
                        mock_game_startup):
        main.main()
        mock_clear_screen.assert_called()
        mock_input.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_option_zero(self, mock_input, mock_print):
        main.main()
        mock_input.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_wrong_input(self, mock_input, mock_print):
        main.main()
        mock_input.assert_called()
        mock_print.assert_called()
