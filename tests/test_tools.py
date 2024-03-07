import unittest
from unittest.mock import MagicMock, patch
from oopython.src import tools

class TestTools(unittest.TestCase):
    def test_init_(self):
        self.tools = tools.Tools()


    @patch("tests")
    def test_clear_screen(self, mock_os):
        self.tools.clear_screen()
        mock_os.system.assert_called_with("clear")
