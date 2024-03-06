import tools


class Histogram:

    def __init__(self):
        self.tools = tools.Tools()
        self.histogram = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def add_to_histogram(self, roll):
        self.histogram[roll] += 1
        print(f'added {roll} to histogram')

    def show_histogram(self):
        self.tools.clear_screen()
        print("---How often each number was rolled---")
        for key, value in self.histogram.items():
            if key == 1:
                print(f"Number of ones rolled: {value}")
            elif key == 2:
                print(f"Number of twos rolled: {value}")
            elif key == 3:
                print(f"Number of threes rolled: {value}")
            elif key == 4:
                print(f"Number of fours rolled: {value}")
            elif key == 5:
                print(f"Number of fives rolled: {value}")
            elif key == 6:
                print(f"Number of sixes rolled: {value}")
        self.tools.enter_to_continue()
