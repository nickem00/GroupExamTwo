# unittest for the highscore class
import unittest
import tools
import highscore
from unittest.mock import patch, mock_open


class TestHighscoreClass(unittest.TestCase):

    def test_init(self):
        h = highscore.Highscore()
        self.assertIsInstance(h.tools, tools.Tools)
        self.assertIsInstance(h.highscoreFile, str)
        self.assertTrue(h.highscoreFile.endswith('.txt'))

    @patch('builtins.open', new_callable=mock_open,
           read_data='player1: 50\nplayer2: 80')
    def test_read_highscores(self, mock_open):
        h = highscore.Highscore()
        result = h.read_highscores()
        self.assertEqual(result, {'player1': 50, 'player2': 80})
        self.assertEqual(mock_open.call_count, 1)
        mock_open.assert_called_with(h.highscoreFile, 'r')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_highscores_no_file(self, mock_open):
        h = highscore.Highscore()
        result = h.read_highscores()
        self.assertEqual(result, {})
        self.assertEqual(mock_open.call_count, 1)
        mock_open.assert_called_with(h.highscoreFile, 'r')

    # test of the display_highscores method
    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscores',
           return_value={'player1': 80, 'player2': 50})
    def test_display_highscores(self, mock_read_highscores,
                                mock_enter_to_continue,
                                mock_clear_screen, mock_print):
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