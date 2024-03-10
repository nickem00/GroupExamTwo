import unittest
from unittest.mock import patch
import main
import runpy


class TestMainClass(unittest.TestCase):
    """Test the main module."""

    @patch("builtins.print")
    @patch("playerVsComputer.PlayerVsComputer.game_startup")
    @patch("builtins.input", return_value="1")
    @patch("tools.Tools.clear_screen")
    def test_option_one(
        self, mock_clear_screen, mock_input, mock_game_startup, mock_print
    ):
        """Test the main function with option one."""
        main.main()
        mock_clear_screen.assert_called_once()
        mock_print.assert_called_with("Welcome to the Game!")
        mock_input.assert_called()
        mock_game_startup.assert_called_once()

    @patch("builtins.print")
    @patch("playerVsPlayer.PlayerVsPlayer.game_startup")
    @patch("builtins.input", return_value="2")
    @patch("tools.Tools.clear_screen")
    def test_option_two(
        self, mock_clear_screen, mock_input, mock_game_startup, mock_print
    ):
        """Test the main function with option two."""
        main.main()
        mock_clear_screen.assert_called_once()
        mock_print.assert_called_with("Welcome to the Game!")
        mock_input.assert_called()
        mock_game_startup.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.input", return_value="0")
    def test_option_zero(self, mock_input, mock_print):
        """Test the main function with option zero."""
        main.main()
        mock_input.assert_called()
        mock_print.assert_called()

    @patch("builtins.print")
    @patch("builtins.input", side_effect=("4", "0"))
    @patch("tools.Tools.enter_to_continue")
    def test_wrong_input(self, mock_enter_to_continue, mock_input, mock_print):
        """Test the main function with wrong input."""
        main.main()
        mock_input.assert_called()
        mock_print.assert_called()
        mock_enter_to_continue.assert_called()

    @patch("builtins.input", return_value="0")
    @patch("builtins.print")
    def test_run_as_main(self, mock_print, mock_input):
        """Test the main module as main."""
        runpy.run_module("main", run_name="__main__")
        mock_input.assert_called()
        mock_print.assert_called()
