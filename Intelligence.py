import dice
import random


class Intelligence:

    def init(self):
        self.intelligence_name = "Computer"
        self.difficulty = 0
        self.total_score = 0
        self.round_score = 0
        self.die = dice.Dice()

    def start_round(self,difficulty):
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

    def easy(self):
        random_hold_easy = random.randint(1, 5)
        self.hold()

    def medium(self):
        random_hold_medium = random.randint(1, 10)
        self.hold()

    def hard(self):
        random_hold_hard = random.randint(1, 20)
        self.hold()
    
