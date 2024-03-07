from oopython.src import tools
import unittest
from oopython.src import developer
from oopython.src import player
from unittest.mock import patch


class TestDeveloperClass(unittest.TestCase):

    '''
    Test the constructor of the Developer class and its attributes.
    '''
    def test_init(self):
        d = developer.Developer()
        self.assertEqual(d.password, 'asd')
        self.assertIsInstance(d.tools, tools.Tools)

    '''
    Test the developer_menu method of the Developer class.
    It tests if the total score of the player is set to 100 and if the
    correct message is printed. It also tests if the clear_screen and
    enter_to_continue methods are called.
    Using patch to mock the input and print functions.
    '''
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

    '''
    Test the developer_menu method of the Developer class when the
    password is wrong. It tests if the total score of the player is not
    changed and if the name of the player is not changed.
    Using patch to mock the input function.
    '''
    def test_developer_menu_wrong_password(self):
        d = developer.Developer()
        p = player.Player('Test')
        p.name = 'Test'

        with patch('builtins.input', return_value='wrong'):
            d.developer_menu(p)

        self.assertEqual(p.total_score, 0)
        self.assertEqual(p.name, 'Test')

    '''
    Test the developer_menu method of the Developer class when the
    the user chooses to go back. It tests if the total score of the player
    is not changed and if the name of the player is not changed.
    '''
    def test_go_back(self):
        d = developer.Developer()
        p = player.Player('Test')
        p.name = 'Test'

        with patch('builtins.input', side_effect=['asd', '2']):
            d.developer_menu(p)

        self.assertEqual(p.total_score, 0)
        self.assertEqual(p.name, 'Test')
