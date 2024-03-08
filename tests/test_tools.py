import unittest
from unittest.mock import MagicMock, patch
from oopython.src import tools

class TestTools(unittest.TestCase):
    def test_init_(self):
        self.tools = tools.Tools()

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
         print_message = self.assertRaises(SystemExit, self.tools.close_game)
         self.assertEqual(str(print_message.argv[0]), "Thank you for playing!")

    @patch("time.sleep")
    def test_pause(self, mock_time_sleep):
         pause_duration = 2
         self.tools.pause(pause_duration)
         mock_time_sleep.assert_called_with(pause_duration)

    
    def test_enter_to_continue(self):
         with patch("builtins.input", return_value = ""):
                with patch.object(tools.Tools, "clear_screen"):
                    self.tools.enter_to_continue()
                    self.tools.clear_screen.assert_called_with()
