import os
import sys
import time


class Tools():

    def __init__(self):
        pass

    '''Simple method for clearing the screen for visual purposes'''
    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    '''Simple method for closing the game.'''
    def close_game(self):
        print('Thank you for playing!')
        sys.exit()

    '''Simple method for pausing the game.'''
    def pause(self, seconds):
        time.sleep(seconds)
        return

    '''Simple method for printing the main menu.'''
    def enter_to_continue(self):
        input('Press enter to continue...')
        self.clear_screen()
        return
