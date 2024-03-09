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