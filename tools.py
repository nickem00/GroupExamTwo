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

    def close_game(self):
        print('Thank you for playing!')
        sys.exit()

    def pause(self, seconds):
        time.sleep(seconds)
        return

    def enter_to_continue(self):
        input('Press enter to continue...')
        self.clear_screen()
        return
