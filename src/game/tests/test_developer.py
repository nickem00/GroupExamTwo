import unittest
import developer
import tools
from unittest.mock import patch
import player


class TestDeveloperClass(unittest.TestCase):
    """Test the Developer class."""

    def test_init(self):
        """Test the __init__ method."""
        d = developer.Developer()
        self.assertEqual(d.password, "asd")
        self.assertIsInstance(d.tools, tools.Tools)

    @patch("builtins.input", side_effect=["asd", "1"])
    @patch("tools.Tools.clear_screen")
    @patch("tools.Tools.enter_to_continue")
    @patch("builtins.print")
    def test_option_one(
        self, mock_print, mock_enter_to_continue, mock_clear_screen, mock_input
    ):
        """
        Test the developer_menu method. The user enters the correct
        password and selects option 1.
        """
        d = developer.Developer()
        p = player.Player("test")
        d.developer_menu(p)
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        self.assertEqual(p.name, "test")
        self.assertEqual(p.total_score, 100)
        mock_enter_to_continue.assert_called()
        mock_clear_screen.assert_called()

    @patch("builtins.input", side_effect=["asd", "2"])
    @patch("tools.Tools.clear_screen")
    def test_option_two(self, mock_clear_screen, mock_input):
        """
        Test the developer_menu method. The user enters the correct
        password and selects option 2.
        """
        d = developer.Developer()
        p = player.Player("test")
        d.developer_menu(p)
        mock_clear_screen.assert_called()
        self.assertEqual(p.name, "test")
        self.assertEqual(p.total_score, 0)
