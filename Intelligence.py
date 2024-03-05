import dice
# import random


class Intelligence:

    def init(self):
        self.intelligence_name = "Computer"
        self.difficulty = 0
        self.total_score = 0
        self.round_score = 0
        self.die = dice.Dice()

    def start_round(difficulty):
        if difficulty == 1:
            pass

        elif difficulty == 2:
            print("Medium")

        elif difficulty == 3:
            print("Hard")

    def hold(self):
        self.total_score += self.round_score
        self.round_score == 0
        return

    def easy():
        pass

    def medium():
        pass

    def hard():
        pass
