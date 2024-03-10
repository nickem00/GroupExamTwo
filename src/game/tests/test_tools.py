import unittest
from unittest.mock import patch
import tools


class TestToolsClass(unittest.TestCase):
    """Test the Tools class."""

    @patch("os.system")
    @patch("os.name", "nt")
    def test_clear_screen_windows(self, mock_system):
        """Test the clear_screen method on Windows."""
        t = tools.Tools()
        t.clear_screen()
        mock_system.assert_called_with("cls")

    @patch("os.system")
    @patch("os.name", "posix")
    def test_clear_screen_linux(self, mock_system):
        """Test the clear_screen method on Linux."""
        t = tools.Tools()
        t.clear_screen()
        mock_system.assert_called_with("clear")

    @patch("sys.exit")
    @patch("builtins.print")
    def test_close_game(self, mock_print, mock_exit):
        """Test the close_game method."""
        t = tools.Tools()
        t.close_game()
        mock_print.assert_called_with("Thank you for playing!")
        mock_exit.assert_called()

    @patch("time.sleep")
    def test_pause(self, mock_sleep):
        """Test the pause method."""
        t = tools.Tools()
        t.pause(2)
        mock_sleep.assert_called_with(2)

    @patch("tools.Tools.clear_screen")
    @patch("builtins.input")
    def test_enter_to_continue(self, mock_input, mock_clear_screen):
        """Test the enter_to_continue method."""
        t = tools.Tools()
        t.enter_to_continue()
        mock_input.assert_called()
        mock_clear_screen.assert_called()
