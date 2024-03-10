import dice
import random
from exceptions import RolledAOneException
import tools


class Intelligence:
    """
    The Intelligence class is for the computer player. It contains
    methods for starting the round, holding, and the different
    difficulties. It also contains methods for rolling the die and
    checking if the computer has won.
    """

    def __init__(self):
        """
        The constructor for the Intelligence class. It sets the name to
        'Computer', the difficulty to 0, the total score to 0, the round
        score to 0, the roll until hold to 0, creates a new dice object,
        and creates a new tools object.
        """
        self.name = "Computer"
        self.difficulty = 0
        self.total_score = 0
        self.round_score = 0
        self.roll_until_hold = 0
        self.die = dice.Dice()
        self.rolls = []
        self.tools = tools.Tools()

    def start_round(self, difficulty, histogram):
        """
        A method for starting the round. It takes in the difficulty and
        the histogram. It then calls the appropriate difficulty method.
        """
        if difficulty == 1:
            self.easy(histogram)
        elif difficulty == 2:
            self.medium(histogram)
        elif difficulty == 3:
            self.hard(histogram)
        else:
            print("Error: Difficulty not set")

    def hold(self):
        """
        A method for holding the round. It adds the round score to the
        total score and sets the round score to 0. It also prints the
        rolls and the round score. It also resets the rolls
        list to an empty list.
        """
        self.total_score += self.round_score
        print(
            f"{self.name} got {self.rolls} in this round!\n"
            f"which gives a total of {self.round_score} points!"
        )
        print("-----------------------------------")
        self.round_score = 0
        self.rolls = []
        return

    def easy(self, histogram):
        """
        A method for starting the easy difficulty. It takes in the
        histogram and rolls the die until a hold is called or a one is
        rolled.
        """
        self.roll_until_hold = random.randint(1, 2)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die(histogram)
            except RolledAOneException:
                print("The computer rolled a one. No points added!")
                break
        self.hold()

    def medium(self, histogram):
        """The same as the easy method, but with a higher roll_until_hold."""
        self.roll_until_hold = random.randint(1, 5)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die(histogram)
            except RolledAOneException:
                print("The computer rolled a one. No points added!")
                break
        self.hold()

    def hard(self, histogram):
        """
        The same as the easy method, but with an even higher roll_until_hold.
        """
        self.roll_until_hold = random.randint(1, 10)
        for _ in range(self.roll_until_hold):
            try:
                self.roll_die(histogram)
            except RolledAOneException:
                print("The computer rolled a one. No points added!")
                break
        self.hold()

    def roll_die(self, histogram):
        """
        A method for rolling the die. It adds the roll to the histogram
        and checks if the roll is a 1. If it is, it sets the round score
        to 0 and raises a RolledAOneException. If it is not, it adds the
        roll to the round score and appends the roll to the rolls list.
        """
        rollNumber = self.die.roll()
        histogram.add_to_histogram(rollNumber)
        if rollNumber == 1:
            self.rolls.append(rollNumber)
            self.round_score = 0
            raise RolledAOneException
        else:
            self.round_score += rollNumber
            self.rolls.append(rollNumber)

    def is_winning(self, winning_score):
        """A method for checking if the computer has won."""
        return self.total_score >= winning_score
