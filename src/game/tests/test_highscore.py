# unittest for the highscore class
import unittest
import tools
import highscore
from unittest.mock import patch, mock_open


class TestHighscoreClass(unittest.TestCase):
    """Tests of the Highscore class."""

    def test_init(self):
        """Tests the constructor for the Highscore class."""
        h = highscore.Highscore()
        self.assertIsInstance(h.tools, tools.Tools)
        self.assertIsInstance(h.highscoreFile, str)
        self.assertTrue(h.highscoreFile.endswith('.txt'))

    @patch('builtins.open', new_callable=mock_open,
           read_data='player1: 50\nplayer2: 80')
    def test_read_highscores(self, mock_open):
        """
        Tests the read_highscores method. Mocks the open function to
        return a file with highscores.
        """
        h = highscore.Highscore()
        result = h.read_highscores()
        self.assertEqual(result, {'player1': 50, 'player2': 80})
        self.assertEqual(mock_open.call_count, 1)
        mock_open.assert_called_with(h.highscoreFile, 'r')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_highscores_no_file(self, mock_open):
        """
        Tests the read_highscores method when the file is not found.
        """
        h = highscore.Highscore()
        result = h.read_highscores()
        self.assertEqual(result, {})
        self.assertEqual(mock_open.call_count, 1)
        mock_open.assert_called_with(h.highscoreFile, 'r')

    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 80, 'player2': 50})
    def test_display_highscores(self, mock_read_highscores,
                                mock_enter_to_continue,
                                mock_clear_screen, mock_print):
        """Tests the display_highscores method."""
        h = highscore.Highscore()
        h.display_highscores()
        mock_clear_screen.assert_called()
        expected_output = [
            unittest.mock.call('Highscores:'),
            unittest.mock.call('-----------\n'),
            unittest.mock.call('1. player1: 80'),
            unittest.mock.call('2. player2: 50')
        ]

        mock_print.assert_has_calls(expected_output, any_order=False)
        mock_enter_to_continue.assert_called()

    @patch('builtins.print')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscores', return_value=None)
    def test_display_highscores_no_highscores(self, mock_read_highscores,
                                              mock_enter_to_continue,
                                              mock_print):
        """Tests the display_highscores method when there are no highscores."""
        h = highscore.Highscore()
        h.display_highscores()
        mock_print.assert_called_with('No highscores found.')
        mock_enter_to_continue.assert_called()

    @patch('builtins.print')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 50, 'player2': 80})
    @patch('builtins.open', new_callable=mock_open)
    def test_save_new_highscore_no_new_highscore(self, mock_open,
                                                 mock_read_highscores,
                                                 mock_enter_to_continue,
                                                 mock_print):
        """
        Tests the save_new_highscore method when the player does not have
        a new highscore.
        """
        h = highscore.Highscore()
        h.save_new_highscore('player1', 40)
        mock_open.assert_called_with(h.highscoreFile, 'w')
        mock_enter_to_continue.assert_not_called()
        mock_print.assert_not_called()

    @patch('builtins.print')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 50, 'player2': 80})
    @patch('builtins.open', new_callable=mock_open)
    def test_save_new_highscore_new_highscore(self, mock_open,
                                              mock_read_highscores,
                                              mock_enter_to_continue,
                                              mock_print):
        """
        Tests the save_new_highscore method when the player has
        a new highscore.
        """
        h = highscore.Highscore()
        h.save_new_highscore('player1', 60)
        mock_open.assert_called_with(h.highscoreFile, 'w')
        mock_enter_to_continue.assert_called()

    @patch('builtins.print')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 50, 'player2': 80})
    @patch('builtins.open', new_callable=mock_open)
    def test_save_new_highscore_new_player(self, mock_open,
                                           mock_read_highscores,
                                           mock_enter_to_continue,
                                           mock_print):
        """
        Tests the save_new_highscore method when the player is new.
        """
        h = highscore.Highscore()
        h.save_new_highscore('player3', 60)
        mock_open.assert_called_with(h.highscoreFile, 'w')
        mock_enter_to_continue.assert_called()

    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 50, 'player2': 80})
    def test_is_highscore_true(self, mock_read_highscores):
        """
        Tests the is_highscore method when the player has a new highscore.
        """
        h = highscore.Highscore()
        result = h.is_highscore('player1', 90)
        self.assertTrue(result)

    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 50, 'player2': 80})
    def test_is_highscore_false(self, mock_read_highscores):
        """
        Tests the is_highscore method when the player does not have
        a new highscore.
        """
        h = highscore.Highscore()
        result = h.is_highscore('player1', 40)
        self.assertFalse(result)

    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 50, 'player2': 80})
    def test_is_highscore_true_empty(self, mock_read_highscores):
        """Tests the is_highscore method when the highscores are empty."""
        h = highscore.Highscore()
        result = h.is_highscore('player3', 40)
        self.assertTrue(result)
