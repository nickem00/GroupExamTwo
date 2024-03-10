# unittest for the histogram class
import unittest
import histogram
from unittest.mock import MagicMock, patch


class TestHistogramClass(unittest.TestCase):
    """Test the Histogram class."""

    def test_init(self):
        """Test the __init__ method (Constructor)."""
        h = histogram.Histogram()
        self.assertEqual(h.histogram, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})

    def test_add_to_histogram(self):
        """Test the add_to_histogram method."""
        h = histogram.Histogram()
        h.add_to_histogram(1)
        self.assertEqual(h.histogram[1], 1)
        self.assertEqual(h.histogram[2], 0)

    @patch('builtins.print')
    def test_show_histogram(self, mock_print):
        """Test the show_histogram method."""
        h = histogram.Histogram()
        h.tools.clear_screen = MagicMock()
        h.tools.enter_to_continue = MagicMock()
        h.histogram = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
        h.show_histogram()
        h.tools.clear_screen.assert_called()
        h.tools.enter_to_continue.assert_called()

        expected_calls = [
            unittest.mock.call("---How often each number was rolled---"),
            unittest.mock.call("Number of ones rolled: 1"),
            unittest.mock.call("Number of twos rolled: 2"),
            unittest.mock.call("Number of threes rolled: 3"),
            unittest.mock.call("Number of fours rolled: 4"),
            unittest.mock.call("Number of fives rolled: 5"),
            unittest.mock.call("Number of sixes rolled: 6"),
        ]

        mock_print.assert_has_calls(expected_calls, any_order=True)
