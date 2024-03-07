import unittest
from oopython.src import histogram
from oopython.src import tools
from unittest.mock import patch


class TestHistogramClass(unittest.TestCase):

    def test_init(self):
        h = histogram.Histogram()
        self.assertIsInstance(h.tools, tools.Tools)
        self.assertEqual(h.histogram, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})

    def test_add_to_histogram(self):
        h = histogram.Histogram()
        h.add_to_histogram(1)
        self.assertEqual(h.histogram[1], 1)

    @patch('builtins.print')
    @patch('tools.Tools.clear_screen')
    @patch('tools.Tools.enter_to_continue')
    def test_show_histogram(self, mock_enter_to_continue,
                            mock_clear_screen, mock_print):
        h = histogram.Histogram()
        h.histogram = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
        h.show_histogram()
        mock_clear_screen.assert_called()
        mock_print.assert_called()
        mock_enter_to_continue.assert_called()
