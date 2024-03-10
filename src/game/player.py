import dice
from exceptions import RolledAOneException
import tools


class Player:
    """
    The Player class is a class for the player. It contains methods for
    rolling the die, holding the round, checking if the player has won,
    and setting the name of the player.
    """

    def __init__(self, name):
        """
        Constructor for the Player class. It takes in a name and sets the
        total_score and round_score to 0. It also creates a new dice and
        tools object for the player.
        """
        self.name = name
        self.total_score = 0
        self.round_score = 0
        self.die = dice.Dice()
        self.tools = tools.Tools()

    def roll_die(self, histogram):
        """
        A method for rolling the die. It adds the roll to the histogram
        and checks if the roll is a 1. If it is, it sets the round score
        to 0 and raises a RolledAOneException. If it is not, it adds the
        roll to the round score and returns the roll.
        """
        rollNumber = self.die.roll()
        histogram.add_to_histogram(rollNumber)
        if rollNumber == 1:
            self.round_score = 0
            raise RolledAOneException
        else:
            self.round_score += rollNumber
        return rollNumber

    def hold(self, highscores):
        """
        A method for holding the round. It adds the round score to the
        total score and saves the new highscore. It then sets the round
        score to 0, to be ready for the next round.
        """
        self.total_score += self.round_score
        highscores.save_new_highscore(self.name, self.round_score)
        self.round_score = 0
        return

    def is_winning(self, winning_score):
        """
        A method for checking if the player has won. It takes in the
        winning score and checks if the total score is greater than or
        equal to the winning score. If it is, it returns True, else it
        returns False.
        """
        return self.total_score >= winning_score

    def set_name(self, name):
        """A method for setting the name of the player."""
        self.name = name
