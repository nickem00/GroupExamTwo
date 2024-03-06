import dice
import random
from exceptions import RolledAOneException
import tools


class Intelligence:

    '''
    Constructor of the Intelligence class.
    '''
    def __init__(self):
        self.name = "Computer"
        self.difficulty = 0
        self.total_score = 0
        self.round_score = 0
        self.roll_until_hold = 0
        self.die = dice.Dice()
        self.rolls = []
        self.tools = tools.Tools()

    '''
    A method for starting the round. It takes in the difficulty
    and the histogram. It then starts the round based on the
    difficulty.
    '''
    def start_round(self, difficulty, histogram):
        self.rolls = []
        if difficulty == 1:
            self.easy(histogram)
        elif difficulty == 2:
            self.medium(histogram)
        elif difficulty == 3:
            self.hard(histogram)
        else:
            print('Error: Difficulty not set')

    '''
    A method for holding the current score. It adds the round score
    to the total score and sets the round score to 0.
    '''
    def hold(self):
        self.total_score += self.round_score
        print(f'{self.name} got {self.rolls} in this round!\n'
              f'which gives a total of {self.round_score} points!')
        print('-----------------------------------')
        self.round_score = 0
        return

    '''
    A method for starting the easy difficulty.
    It takes in the histogram and rolls the die until
    a hold is called or a one is rolled.
    '''
    def easy(self, histogram):
        self.roll_until_hold = random.randint(1, 2)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die(histogram)
            except RolledAOneException:
                print('The computer rolled a one. No points added!')
                break
        self.hold()

    '''
    A method for starting the medium difficulty.
    It takes in the histogram and rolls the die until
    a hold is called or a one is rolled.
    '''
    def medium(self, histogram):
        self.roll_until_hold = random.randint(1, 5)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die(histogram)
            except RolledAOneException:
                print('The computer rolled a one. No points added!')
                break
        self.hold()

    '''
    A method for starting the hard difficulty.
    It takes in the histogram and rolls the die until
    a hold is called or a one is rolled.
    '''
    def hard(self, histogram):
        self.roll_until_hold = random.randint(1, 10)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die(histogram)
            except RolledAOneException:
                print('The computer rolled a one. No points added!')
                break
        self.hold()

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
            self.rolls.append(rollNumber)
            self.round_score = 0
            raise RolledAOneException
        else:
            self.round_score += rollNumber
            self.rolls.append(rollNumber)

    '''
    A method for checking if the computer has reached the winning score.'''
    def is_winning(self, winning_score):
        return self.total_score >= winning_score
