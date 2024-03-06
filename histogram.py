import dice

class Histogram:

    def __init__(self):
        self.list_of_6 = []
        self.list_of_5 = []
        self.list_of_4 = []
        self.list_of_3 = []
        self.list_of_2 = []
        self.list_of_1 = []

    def dice_tracker(self):
        roll_number = dice.Dice().roll()

        if roll_number == 6:
            self.list_of_6.append(6)
        elif roll_number == 5:
            self.list_of_5.append(5)
        elif roll_number == 4:
            self.list_of_4.append(4)
        elif roll_number == 3:
            self.list_of_3.append(3)
        elif roll_number == 2:
            self.list_of_2.append(2)
        elif roll_number == 1:
            self.list_of_1.append(1)

    def show_statistics(self):
        print("---How often each number was rolled---")
        amount_of_6 = len(self.list_of_6)
        amount_of_5 = len(self.list_of_5)
        amount_of_4 = len(self.list_of_4)
        amount_of_3 = len(self.list_of_3)
        amount_of_2 = len(self.list_of_2)
        amount_of_1 = len(self.list_of_1)
        print(f"Number of sixes rolled: {amount_of_6}")
        print(f"Number of fives rolled: {amount_of_5}")
        print(f"Number of fours rolled: {amount_of_4}")
        print(f"Number of threes rolled: {amount_of_3}")
        print(f"Number of twos rolled: {amount_of_2}")
        print(f"Number of ones rolled: {amount_of_1}")


    