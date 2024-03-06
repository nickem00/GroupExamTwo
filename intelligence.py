import dice
import random


class Intelligence:

    def __init__(self):
        self.intelligence_name = "Computer"
        self.difficulty = 0
        self.total_score = 0
        self.round_score = 0
        self.roll_until_hold = 0
        self.die = dice.Dice()

    def start_round(self, difficulty):
        if difficulty == 1:
            self.easy()
        elif difficulty == 2:
            print("Medium")
        elif difficulty == 3:
            print("Hard")

    def hold(self):
        self.total_score += self.round_score
        self.round_score = 0
        return

    def easy(self):
        self.roll_until_hold = random.randint(1, 6)
        for i in range(self.roll_until_hold):
            self.roll_die()
        self.hold()

    def medium(self):
        self.roll_until_hold = random.randint(1, 11)
        for i in range(self.roll_until_hold):
            self.roll_die()

        self.hold()

    def hard(self):
        self.roll_until_hold = random.randint(1, 21)

        for i in range(self.roll_until_hold):
            self.roll_die()
        self.hold()

    def roll_die(self):
        rollNumber = self.die.roll()
        if rollNumber == 1:
            self.round_score = 0
        else:
            self.round_score += rollNumber
        return rollNumber
