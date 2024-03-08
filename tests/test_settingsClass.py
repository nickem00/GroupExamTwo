import unittest
from oopython.src import settingsClass
from unittest.mock import patch


class TestSettingsClass(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_change_difficulty(self, mock_input):
        s = settingsClass.SettingsClass()
        new_difficulty = s.change_difficulty()
        mock_input.assert_called()
        self.assertEqual(new_difficulty, 1)
