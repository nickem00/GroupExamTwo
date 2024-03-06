import os
import sys


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
