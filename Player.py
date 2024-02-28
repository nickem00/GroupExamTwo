import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.round_score = 0
        self.die = Dice.Dice()

    def roll_die(self):
        rollNumber = self.die.roll()
        if rollNumber == 1:
            self.round_score == 0
        else:
            self.round_score += 0
        return rollNumber
    
    def hold(self):
        self.total_score += self.round_score
        return
    
    def is_winning(self, winning_score)
        return self.total_score >= winning_score