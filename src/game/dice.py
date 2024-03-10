import random


class Dice:
    """
    A class representing a dice. It has a method for rolling the die.
    """

    def __init__(self):
        """
        The constructor for the Dice class. It sets the number of sides to 6.
        """
        self.sides = 6

    def roll(self):
        """
        A method for rolling the die. It returns a random number between 1 and
        the number of sides.
        """
        return random.randint(1, self.sides)
# test
