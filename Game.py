import os
import player
import time
import tools


class Game():

    '''Constructor of the Game class.'''
    def __init__(self):
        self.computer_player = player.Player('Computer')
        self.human_player = None
        self.tools = tools.Tools()

    '''
    A method for starting up the game. Also prints the main menu and
    promts the user to select an option.
    '''
    def game_startup(self):
        self.tools.clear_screen()
        print('Welcome to PIG Dice Game!')
        self.human_player = player.Player(input('Please enter your name >> '))

        main_menu_options = {
            '1': ('Start Game', self.start_game),
            '2': ('Show Rules', self.show_rules),
            '3': ('Change Name', self.change_name),
            '4': ('Exit Game', None)
        }

        while True:
            self.print_main_menu(main_menu_options)
            try:
                choice = int(input('>>> '))
            except ValueError:

                print('Please enter a valid choice! Error: Not a number')
                time.sleep(2)
                continue

            if 1 <= choice <= 4:
                if choice == 4:
                    return
                elif main_menu_options[str(choice)][1]:
                    main_menu_options[str(choice)][1]()
                else:
                    print('This option is not implemented yet.')
            else:
                print('Please enter a valid choice!')

    '''A method for showing the rules of the game.'''
    def show_rules(self):
        pass

    '''A method for changing the player name.'''
    def change_name(self):
        self.human_player.set_name(input('Please enter new name >> '))

    '''A method for printing the menu'''
    def print_main_menu(self, main_menu_options):
        print()
        print(f'Welcome {self.human_player.name}')
        for key in main_menu_options:
            print(f'{key}. {main_menu_options[key][0]}')

    def print_game_menu(self, game_menu_options):
        print()
        for key in game_menu_options:
            print(f'{key}. {game_menu_options[key][0]}')

    '''Starts the actual game'''
    def start_game(self):
        game_menu_options = {
            '1': ('Roll die', self.human_player.roll_die),
            '2': ('Hold', self.human_player.hold),
            '3': ('Exit game', None)
        }

        rounds = 0
        if rounds == 0:
            print(f'You start {self.human_player.name}!')

        while True:
            self.print_game_menu(game_menu_options)
            try:
                choice = int(input('>>> '))
            except ValueError:
                print('Please enter a valid choice! Error: Not a number')
                time.sleep(2)
                continue

            if 1 <= choice <= 4:
                if choice == 3:
                    return
                elif choice == 1:
                    current_roll = game_menu_options[str(choice)][1]()
                    print(f'You rolled a {current_roll}')
                else:
                    pass
            else:
                print('Please enter a valid choice')
