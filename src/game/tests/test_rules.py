import unittest
import tools
import rules
from unittest.mock import patch


class TestRulesClass(unittest.TestCase):
    """Test the Rules class."""

    def test_init(self):
        """Tests the constructor for the Rules class."""
        r = rules.Rules()
        self.assertIsInstance(r.tools, tools.Tools)

    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    def test_show_rules(self, mock_enter_to_continue,
                        mock_clear_screen, mock_print):
        """Test the show_rules method."""
        r = rules.Rules()
        r.show_rules()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_enter_to_continue.assert_called()
