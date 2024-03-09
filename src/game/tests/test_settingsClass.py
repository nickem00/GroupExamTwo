import unittest
import settingsClass
from unittest.mock import patch


class TestSettingsClass(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input')
    def test_change_difficulty(self, mock_input, mock_print):
        s = settingsClass.SettingsClass()
        s.change_difficulty()
        mock_input.assert_called()
