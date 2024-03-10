import tools


class Histogram:
    """
    A class to represent a histogram of dice rolls. The histogram attribute is
    a dictionary with the numbers 1-6 as keys and the number of times each
    number was rolled as values.
    """

    def __init__(self):
        """The constructor for the Histogram class. Initializes the tools
        attribute and the histogram attribute. The histogram attribute is a
        dictionary with the numbers 1-6 as keys and the number of times each
        number was rolled as values.
        """
        self.tools = tools.Tools()
        self.histogram = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def add_to_histogram(self, roll):
        """A method for adding to the histogram. Takes a roll as an argument
        and adds 1 to the value of the key that corresponds to the number
        rolled.
        """
        self.histogram[roll] += 1

    def show_histogram(self):
        """
        A method for displaying the histogram. This method uses the tools
        attribute to clear the screen and then prints out the number of times
        each number was rolled.
        """
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
