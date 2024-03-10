import unittest
import settingsClass
from unittest.mock import patch


class TestSettingsClass(unittest.TestCase):
    """Test the Settings class."""

    @patch('builtins.print')
    @patch('builtins.input')
    def test_change_difficulty(self, mock_input, mock_print):
        """Test the change_difficulty method."""
        s = settingsClass.SettingsClass()
        s.change_difficulty()
        mock_input.assert_called()
