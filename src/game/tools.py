import os
import sys
import time


class Tools:
    """
    This class contains different 'tools' that can be used in the game,
    such as clearing the screen, closing the game, pausing the game for
    a certain amount of time, and the enter_to_continue method which
    pauses the game until the user presses enter.
    """

    def __init__(self):
        """
        Just a simple constructor method that does nothing but create
        an instance of the class.
        """
        pass

    def clear_screen(self):
        """
        This method clears the screen. It uses the os module to check
        the operating system and then uses the appropriate command to
        clear the screen.
        """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def close_game(self):
        """
        A simple method for closing the game. It prints a message and
        then exits the game. It uses the sys module to exit from
        anywhere in the game.
        """
        print("Thank you for playing!")
        sys.exit()

    def pause(self, seconds):
        """
        A simple method for pausing the game for a certain amount of time.
        It uses the time module to pause the game.
        """
        time.sleep(seconds)
        return

    def enter_to_continue(self):
        """
        A simple method for pausing the game until the user presses enter.
        It uses the built-in input function to pause the game.
        When the user presses enter, the game continues, and the screen
        is cleared.
        """
        input("Press enter to continue...")
        self.clear_screen()
        return
