import unittest
import dice
from unittest.mock import patch, MagicMock

class test_dice(unittest.TestCase):

   def test_init_(self):
      d = dice.Dice()
      self.assertIsInstance(d, dice.Dice)

   def test_roll(self):
      d = dice.Dice()
      result = d.roll()
      self.assertTrue(1 <= result <= 6)
      

   


      
      
