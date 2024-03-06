import dice
import random
from exceptions import RolledAOneException
import tools


class Intelligence:

    def __init__(self):
        self.name = "Computer"
        self.difficulty = 0
        self.total_score = 0
        self.round_score = 0
        self.roll_until_hold = 0
        self.die = dice.Dice()
        self.rolls = []
        self.tools = tools.Tools()

    def start_round(self, difficulty):
        self.rolls = []
        if difficulty == 1:
            self.easy()
        elif difficulty == 2:
            self.medium()
        elif difficulty == 3:
            self.hard()
        else:
            print('Error: Difficulty not set')

    def hold(self):
        self.total_score += self.round_score
        print(f'{self.name} got {self.rolls} in this round!\n'
              f'which gives a total of {self.round_score} points!')
        print('-----------------------------------')
        self.round_score = 0
        return

    def easy(self):
        self.roll_until_hold = random.randint(1, 2)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die()
            except RolledAOneException:
                print('The computer rolled a one. No points added!')
                break
        self.hold()

    def medium(self):
        self.roll_until_hold = random.randint(1, 5)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die()
            except RolledAOneException:
                break
        self.hold()

    def hard(self):
        self.roll_until_hold = random.randint(1, 10)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die()
            except RolledAOneException:
                break
        self.hold()

    def roll_die(self):
        rollNumber = self.die.roll()
        if rollNumber == 1:
            self.rolls.append(rollNumber)
            self.round_score = 0
            raise RolledAOneException
        else:
            self.round_score += rollNumber
            self.rolls.append(rollNumber)

    def is_winning(self, winning_score):
        return self.total_score >= winning_score
