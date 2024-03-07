import unittest
from unittest.mock import patch
from oopython.src import main
from unittest.mock import MagicMock


class TestMainClass(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_option_one(self):
        main.tools.Tools.clear_screen = MagicMock()
        main.playerVsComputer.PlayerVsComputer.game_startup = MagicMock()
        main.main()
        main.tools.Tools.clear_screen.assert_called()
        main.playerVsComputer.PlayerVsComputer.game_startup.assert_called()

    @patch('builtins.input', side_effect=['2'])
    def test_option_two(self):
        main.tools.Tools.clear_screen = MagicMock()
        main.playerVsPlayer.PlayerVsPlayer.game_startup = MagicMock()
        main.main()
        main.tools.Tools.clear_screen.assert_called()
        main.playerVsPlayer.PlayerVsPlayer.game_startup.assert_called()

    @patch('builtins.input', side_effect=['0'])
    def test_option_zero(self):
        main.tools.Tools.clear_screen = MagicMock()
        main.main()
        main.tools.Tools.clear_screen.assert_called()

    @patch('builtins.input', side_effect=['3', '1'])
    @patch('builtins.print')
    def test_invalid_option(self, mock_print):
        main.tools.Tools.clear_screen = MagicMock()
        main.main()
        main.tools.Tools.clear_screen.assert_called()
        mock_print.assert_called()
