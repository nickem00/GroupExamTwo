import unittest
from oopython.src import highscore
from unittest.mock import patch, mock_open
from oopython.src import tools


class TestHighscoreClass(unittest.TestCase):

    def test_init(self):
        h = highscore.Highscore()
        self.assertIsInstance(h.tools, tools.Tools)
        self.isinstance(h.highscoreFile, str)
        self.assertTrue(h.highscoreFile.endswith('.txt'))

    @patch('builtins.open', new_callable=mock_open,
           read_data='player1: 50\nplayer2: 80')
    def test_read_highscore(self, mock_open):
        h = highscore.Highscore()
        result = h.read_highscore()
        self.assertEqual(result, {'player1': 50, 'player2': 80})
        self.assertEqual(mock_open.call_count, 1)
        mock_open.assert_called_with(h.highscoreFile, 'r')

    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    @patch('highscore.Highscore.read_highscore',
           return_value={'player1': 50, 'player2': 80})
    def test_display_highscores(self, mock_enter_to_continue,
                                mock_clear_screen, mock_print):
        h = highscore.Highscore()
        h.display_highscores()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_enter_to_continue.assert_called()

    @patch('highscore.Highscore.read_highscore',
           return_value={'player1': 50, 'player2': 80})
    def test_is_highscore(self):
        h = highscore.Highscore()
        self.assertTrue(h.is_highscore('player1', 60))

    @patch('highscore.Highscore.read_highscore',
           return_value={'player1': 50, 'player2': 80})
    def test_is_not_highscore(self):
        h = highscore.Highscore()
        self.assertFalse(h.is_highscore('player1', 40))