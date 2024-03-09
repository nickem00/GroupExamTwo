import unittest
from unittest.mock import patch
import tools
import os


class TestToolsClass(unittest.TestCase):

    @patch('os.system')
    def test_clear_screen(self, mock_system):
        t = tools.Tools()
        t.clear_screen()
        if os.name == 'nt':
            mock_system.assert_called_with('cls')
        else:
            mock_system.assert_called_with('clear')

    @patch("sys.exit")
    @patch("builtins.print")
    def test_close_game(self,mock_print, mock_exit):
        t = tools.Tools()
        t.close_game()
        mock_print.assert_called_with('Thank you for playing!')
        mock_exit.assert_called()

    @patch("time.sleep")
    def test_pause(self, mock_sleep):
        t = tools.Tools()
        t.pause(2)
        mock_sleep.assert_called_with(2)

    @patch("tools.Tools.clear_screen")
    @patch("builtins.input")
    def test_enter_to_continue(self, mock_input, mock_clear_screen):
        t = tools.Tools()
        t.enter_to_continue()
        mock_input.assert_called()
        mock_clear_screen.assert_called()



        
