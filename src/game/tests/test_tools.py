import unittest
from unittest.mock import patch, MagickMock
from GroupExamTwo.src import tools

class TestTools(unittest.TestCase):

    @patch("os.name", "nt")
    @patch('os.system')
    def test_clear_screen_windows(self, mock_os_system):
        self.tools.clear_screen()
        mock_os_system.assert_called_with('cls')

    @patch("os.name", "posix")
    @patch('os.system')
    def test_clear_screen_unix(self, mock_os_system):
            self.tools.clear_screen()
            mock_os_system.assert_called_with('clear')

    @patch("sys.exit")
    def test_close_game(self, mock_sys_exit):
         self.tools.close_game()
         mock_sys_exit.assert_called_with()
         self.assertIn("Thank you for playing!", mock_sys_exit.call_args[0][0])

    @patch("time.sleep")
    def test_pause(self, mock_time_sleep):
         pause_duration = 2
         self.tools.pause(pause_duration)
         mock_time_sleep.assert_called_with(pause_duration)

    def test_enter_to_continue(self):
         with patch.object("builtins.input", return_value = ""):
                with patch.object(tools.Tools, "clear_screen"):
                    self.tools.enter_to_continue()
                    self.tools.clear_screen.assert_called_with()