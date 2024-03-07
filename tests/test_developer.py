from oopython.src import tools
import unittest
from oopython.src import developer
from oopython.src import player
from unittest.mock import patch


class TestDeveloperClass(unittest.TestCase):

    def test_init(self):
        d = developer.Developer()
        self.assertEqual(d.password, 'asd')
        self.assertIsInstance(d.tools, tools.Tools)

    @patch('builtins.input', side_effect=['asd', '1'])
    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    def test_developer_menu(self, mock_enter_to_continue, mock_clear_screen,
                            mock_print, mock_input):
        d = developer.Developer()
        p = player.Player('Test')
        p.name = 'Test'

        d.developer_menu(p)

        self.assertEqual(p.total_score, 100)
        mock_print.assert_called_with('Test now has 100 points')
        mock_enter_to_continue.assert_called()
        mock_clear_screen.assert_called()

    def test_developer_menu_wrong_password(self):
        d = developer.Developer()
        p = player.Player('Test')
        p.name = 'Test'

        with patch('builtins.input', return_value='wrong'):
            d.developer_menu(p)

        self.assertEqual(p.total_score, 0)
        self.assertEqual(p.name, 'Test')

    def test_go_back(self):
        d = developer.Developer()
        p = player.Player('Test')
        p.name = 'Test'

        with patch('builtins.input', side_effect=['asd', '2']):
            d.developer_menu(p)

        self.assertEqual(p.total_score, 0)
        self.assertEqual(p.name, 'Test')
