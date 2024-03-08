import unittest
from unittest.mock import patch, MagicMock
from src import rules
from src import tools

class TestRulesClass(unittest.TestCase):

    def test_init(self):
        r = rules.Rules()
        self.assertIsInstance(r.tools, tools.Tools)
