import intelligence
import player
import settingsClass
import rules
import developer
import histogram
import tools
import time
from exceptions import (RolledAOneException,
                        GameExitException)


class PlayerVsPlayer:

    '''Constructor of the Game class.'''
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.tools = tools.Tools()
        self.difficulty = 1
        self.settings = settingsClass.SettingsClass()
        self.all_rules = rules.Rules()
        self.intelligence = intelligence.Intelligence()
        self.developer = developer.Developer()
        self.histogram = histogram.Histogram()
        self.main_menu_options = [
            '1. Start Game\n',
            '2. Show Rules\n',
            '3. Exit Game\n'
        ]
        self.game_menu_options = [
            '1. Roll\n',
            '2. Hold\n',
            '3. Show Rules\n',
            '4. Change Name\n',
            '5. Show Histogram\n',
            '6. Exit game (Points Reset)\n',
            '7. Developer Menu\n'
        ]

    '''
    A method for starting up the game. Also prints the main menu and
    prompts the user to enter the names of two players.
    '''
    def game_startup(self):
        self.tools.clear_screen()
        print('Welcome to PIG Dice Game!')
        player1_name = input('Please enter the name of Player 1 >> ')
        player2_name = input('Please enter the name of Player 2 >> ')
        self.player_one = player.Player(player1_name)
        self.player_two = player.Player(player2_name)

        while True:
            self.print_main_menu()
            try:
                choice = int(input('>>> '))
            except ValueError:
                print('Please enter a valid choice! Error: Not a number')
                time.sleep(2)
                continue

            if 1 <= choice <= 3:
                if choice == 3:
                    self.tools.close_game()
                elif choice == 2:
                    self.all_rules.show_rules()
                else:
                    self.start_game()
            else:
                print('Please enter a valid choice! Error: Not in range 1-3')
                continue

    def start_game(self):
        rounds = 0
        while True:
            try:
                if rounds % 2 == 0:
                    self.start_round(rounds, self.player_one)
                    rounds += 1
                else:
                    self.start_round(rounds, self.player_two)
                    rounds += 1
            except GameExitException:
                self.player_one.total_score = 0
                self.player_two.total_score = 0
                self.show_histogram()
                break

    def start_round(self, rounds, player):
        self.tools.clear_screen()

        while True:
            if rounds == 0:
                print(f'{player.name} goes first!')
            else:
                print(f'{player.name}\'s turn!')
            self.print_game_menu()
            try:
                choice = int(input('>>> '))
            except ValueError:
                print('Please enter a valid choice! Error: Not a number')
                time.sleep(3)
                continue

            if 1 <= choice <= 7:
                if choice == 7:
                    self.developer.developer_menu(player)
                elif choice == 6:
                    raise GameExitException
                elif choice == 5:
                    self.histogram.show_histogram()
                elif choice == 4:
                    self.change_name()
                elif choice == 3:
                    self.all_rules.show_rules()
                elif choice == 2:
                    player.hold()
                    self.tools.clear_screen()
                    if player.is_winning(100):
                        print(f'***Congratulations {player.name}!'
                              f' You won!***')
                        self.tools.enter_to_continue()
                        raise GameExitException
                    else:
                        print('You held! Your total score is '
                              f'now {player.total_score}')
                        print('-----------------------------------')
                        self.print_points()
                        self.tools.enter_to_continue()
                        break
                else:
                    try:
                        current_roll = player.roll_die(self.histogram)
                        self.tools.clear_screen()
                        print(f'You rolled a {current_roll}!')
                    except RolledAOneException:
                        print('\nYou rolled a 1! Your turn is over.')
                        self.tools.enter_to_continue()
                        break

    '''
    A method for printing the main menu.
    '''
    def print_main_menu(self):
        print('---Main Menu---\n')
        for option in self.main_menu_options:
            print(option, end='')
        return

    '''
    A method for printing the game menu.
    '''
    def print_game_menu(self):
        print('---Game Menu---\n')
        for option in self.game_menu_options:
            print(option, end='')
        return

    '''
    A method for displaying the rules of the game.
    '''
    def show_rules(self):
        self.all_rules.show_rules()
        return

    def change_name(self):
        while True:
            try:
                self.tools.clear_screen()
                print('Which player would you like to change the name of?')
                print(f'1. {self.player_one.name}\n'
                      f'2. {self.player_two.name}\n')
                choice = int(input('>>> '))
                self.tools.clear_screen()
                if choice == 1:
                    new_name = input('Enter new name for player one: ')
                    self.player_one.set_name(new_name)
                    self.tools.clear_screen()
                    break
                else:
                    new_name = input('Enter new name for player two: ')
                    self.player_two.set_name(new_name)
                    self.tools.clear_screen()
                    break
            except ValueError:
                self.tools.clear_screen()
                print('Please enter a valid choice! Error: Not a number')
                time.sleep(2)
                self.tools.clear_screen()
                continue
        return

    def print_points(self):
        print('Scores:\n'
              f'{self.player_one.name}: '
              f'{self.player_one.total_score}\n'
              f'{self.player_two.name}: '
              f'{self.player_two.total_score}\n')
        return

    def show_histogram(self):
        self.histogram.show_histogram()
        return
