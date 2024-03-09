import unittest
from unittest.mock import MagicMock, patch
import tools

class TestTools(unittest.TestCase):
    
    @patch("tools.Tools.os.system")
    def test_clear_screen_windows(self, mock_system):
        t = tools.Tools()

        


