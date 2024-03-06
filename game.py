# import os
import player
import time
import tools
import intelligence
import rules
import settingsClass
from exceptions import (GameExitException, RolledAOneException,
                        ComputerWonException)
import developer


class Game():

    '''Constructor of the Game class.'''
    def __init__(self):
        self.computer_player = intelligence.Intelligence()
        self.human_player = None
        self.tools = tools.Tools()
        self.difficulty = 1
        self.settings = settingsClass.SettingsClass()
        self.all_rules = rules.Rules()
        self.intelligence = intelligence.Intelligence()
        self.developer = developer.Developer()

    '''
    A method for starting up the game. Also prints the main menu and
    promts the user to select an option.
    '''
    def game_startup(self):
        self.tools.clear_screen()
        print('Welcome to PIG Dice Game!')
        if not self.human_player:
            self.human_player = player.Player(input('Please enter '
                                                    'your name >> '))

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
                    self.tools.close_game()
                elif main_menu_options[str(choice)][1]:
                    main_menu_options[str(choice)][1]()
                else:
                    print('This option is not implemented yet.')
            else:
                print('Please enter a valid choice!')

    '''
    A method for showing the rules of the game.
    '''
    def show_rules(self):
        self.all_rules.show_rules()

    '''
    A method for changing the player name.
    '''
    def change_name(self):
        self.human_player.set_name(input('Please enter new name >> '))

    '''
    A method for printing the Main menu.
    '''
    def print_main_menu(self, main_menu_options):
        print()
        print(f'Welcome {self.human_player.name}')
        for key in main_menu_options:
            print(f'{key}. {main_menu_options[key][0]}')

    def print_game_menu(self, game_menu_options):
        print()
        for key in game_menu_options:
            print(f'{key}. {game_menu_options[key][0]}')

    '''
    A method for starting the game.
    It contains the game loop.
    '''
    def start_game(self):
        game_menu_options = {
            '1': ('Roll die', self.human_player.roll_die),
            '2': ('Hold', self.human_player.hold),
            '3': ('Change Difficulty', self.change_difficulty),
            '4': ('Exit game (Points reset)', None),
            ' ': ('-------------------------', None),
            '5': ('Dev-Options', self.developer.developer_menu)
        }

        rounds = 0
        while True:
            try:
                if rounds % 2 == 0:
                    self.human_players_turn(rounds, game_menu_options)
                    rounds += 1
                else:
                    self.tools.clear_screen()
                    print('Computer players turn!')
                    self.computer_players_turn()
                    rounds += 1
            except (GameExitException, ComputerWonException):
                break

    '''
    A method for the human players turn.
    It takes in the current round and the game menu options.
    '''
    def human_players_turn(self, rounds, game_menu_options):
        if rounds == 0:
            self.tools.clear_screen()
            print(f'You start {self.human_player.name}!')

        while True:
            self.print_game_menu(game_menu_options)
            try:
                choice = int(input('>>> '))
            except ValueError:
                print('Please enter a valid choice! Error: Not a number')
                time.sleep(2)
                continue

            if 1 <= choice <= 5:
                if choice == 4:
                    print('Exiting game..')
                    self.human_player.total_score = 0
                    raise GameExitException
                elif choice == 1:
                    try:
                        current_roll = game_menu_options[str(choice)][1]()
                        self.tools.clear_screen()
                        print(f'You rolled a {current_roll}')
                    except RolledAOneException:
                        print('\nYou rolled a 1! Your turn is over.')
                        input('Press enter to continue...')
                        break
                elif choice == 2:
                    game_menu_options[str(choice)][1]()
                    self.tools.clear_screen()
                    if self.human_player.is_winning(100):
                        print(f'***Congratulations {self.human_player.name}!'
                              'You won!***')
                        self.tools.enter_to_continue()
                        break
                    else:
                        print('You held! Your total score is '
                              f'now {self.human_player.total_score}')
                        print('-----------------------------------')
                        self.print_points()
                        self.tools.enter_to_continue()
                        break
                elif choice == 5:
                    self.developer.developer_menu(self.human_player)
                else:
                    game_menu_options[str(choice)][1]()
            else:
                print('Please enter a valid choice')

    '''
    A method for the computer players turn.
    '''
    def computer_players_turn(self):
        self.computer_player.start_round(self.difficulty)
        if self.computer_player.is_winning(100):
            print('The computer won!')
            self.tools.enter_to_continue()
            raise ComputerWonException
        self.print_points()
        self.tools.enter_to_continue()

    '''
    A method for changing the difficulty of the game.
    '''
    def change_difficulty(self):
        new_difficulty = self.settings.change_difficulty()
        if new_difficulty == self.difficulty:
            print('You selected the same difficulty.')
        else:
            self.difficulty = new_difficulty
            print('You selected a new difficulty!')

    def print_points(self):
        print('Scores:\n'
              f'You: {self.human_player.total_score}\n'
              f'Computer: {self.computer_player.total_score}\n')
