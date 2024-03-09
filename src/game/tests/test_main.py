import unittest
from unittest.mock import patch
import main


class TestMainClass(unittest.TestCase):

    @patch('builtins.print')
    @patch('playerVsComputer.PlayerVsComputer.game_startup')
    @patch('builtins.input', return_value='1')
    @patch('tools.Tools.clear_screen')
    def test_option_one(self, mock_clear_screen,
                        mock_input, mock_game_startup,
                        mock_print):
        main.main()
        mock_clear_screen.assert_called_once()
        mock_print.assert_called_with('Welcome to the Game!')
        mock_input.assert_called()
        mock_game_startup.assert_called_once()


if __name__ == '__main__':
    unittest.main()
