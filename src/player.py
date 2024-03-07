import dice
from exceptions import RolledAOneException
import highscore


class Player:

    '''
    Constructor of the Player class.
    '''
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.round_score = 0
        self.die = dice.Dice()
        self.highscore = highscore.Highscore()

    '''
    A method for rolling the die. It takes in a histogram,
    and rolls the die. It then adds the roll to the histogram.
    If the roll is 1, the round score is set to 0 and a
    RolledAOneException is raised. Otherwise the roll is added
    to the round score and returned.'''
    def roll_die(self, histogram):
        rollNumber = self.die.roll()
        histogram.add_to_histogram(rollNumber)
        if rollNumber == 1:
            self.round_score = 0
            raise RolledAOneException
        else:
            self.round_score += rollNumber
        return rollNumber

    '''
    A method for holding the current score. It adds the round score
    to the total score and sets the round score to 0.'''
    def hold(self):
        self.total_score += self.round_score
        self.highscore.new_highscore(self.name, self.round_score)
        self.round_score = 0
        return

    '''
    A method for checking if the player has reached the winning score.
    '''
    def is_winning(self, winning_score):
        return self.total_score >= winning_score

    '''
    A method for setting the name of the player.'''
    def set_name(self, name):
        self.name = name
