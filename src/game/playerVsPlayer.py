import intelligence
import player
import settingsClass
import highscore
import rules
import developer
import histogram
import tools
import time
from exceptions import (RolledAOneException,
                        GameExitException)


class PlayerVsPlayer:
    """
    The PlayerVsPlayer class is one of the main classes of the game.
    This one is for the player vs player mode.
    It is responsible for the game startup, the game itself, and the
    main menu. The game is turn-based and the players take turns
    playing the game. The game will continue to run until a player
    wins the game or a GameExitException is raised (when the user
    chooses to exit the game).
    """

    def __init__(self):
        """
        The constructor for the PlayerVsPlayer class. It initializes
        the player_one and player_two to None, creates different objects
        used in the game, and initializes the main menu and game menu
        options.
        """
        self.player_one = None
        self.player_two = None
        self.tools = tools.Tools()
        self.difficulty = 1
        self.settings = settingsClass.SettingsClass()
        self.all_rules = rules.Rules()
        self.intelligence = intelligence.Intelligence()
        self.developer = developer.Developer()
        self.histogram = histogram.Histogram()
        self.highscores = highscore.Highscore()
        self.main_menu_options = [
            '1. Start Game\n',
            '2. Show Rules\n'
            '3. Show Highscores\n',
            '4. Exit Game\n'
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

    def game_startup(self):
        """
        The method for the game startup (Main menu). The game is turn-based.
        It prompts the user to enter the names of the players and then
        starts the game. The game will continue to run until the user
        chooses to exit the game. It also has an option to show the
        rules of the game and the highscores.
        """
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

            if 1 <= choice <= 4:
                if choice == 4:
                    self.tools.close_game()
                elif choice == 3:
                    self.highscores.display_highscores()
                elif choice == 2:
                    self.all_rules.show_rules()
                else:
                    self.start_game()
            else:
                print('Please enter a valid choice! Error: Not in range 1-4')
                continue

    def start_game(self):
        """
        This method starts the acual game. It is turn-based and will
        continue to run until a player wins the game or a GameExitException
        is raised (when the user chooses to exit the game). Uses modulos
        to determine which player's turn it is. If the rounds variable
        is even, it is player one's turn, and if it is odd, it is player
        two's turn. Always shows the histogram of the game after the
        GameExitException is raised.
        More details about the game can be found in the start_round method.
        """
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
        """
        This method starts a round of the game. If its the first round,
        it will print which player goes first, otherwise it will print
        which player's turn it is. It will then prompt the user to choose
        an option from the game menu. The game menu has the following
        options:
        1. Roll
        2. Hold
        3. Show Rules
        4. Change Name
        5. Show Histogram
        6. Exit game (Points Reset)
        7. Developer Menu
        If the user chooses to roll, the player will roll the die and
        the current roll will be printed. If the user chooses to hold,
        the player will hold and the total score of the player will be
        printed. If the player is winning, a congratulatory message will
        be printed and a GameExitException will be raised.
        Then there are some options for other small features, such as
        showing the rules, changing the name of a player, showing the
        histogram of the game, and the developer menu. More details about
        these features can be found in the respective methods.
        """
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
                    player.hold(self.highscores)
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

    def print_main_menu(self):
        """
        A simple method for printing the main menu.
        """
        print('---Main Menu---\n')
        for option in self.main_menu_options:
            print(option, end='')
        return

    def print_game_menu(self):
        """
        A simple method for printing the game menu.
        """
        print('---Game Menu---\n')
        for option in self.game_menu_options:
            print(option, end='')
        return

    def show_rules(self):
        """
        A method for showing the rules of the game."""
        self.all_rules.show_rules()
        return

    def change_name(self):
        """
        A method for changing the name of a player. It will prompt the
        user to choose which player to change the name of, and then
        prompt the user to enter the new name. If the user enters a
        number that is not 1 or 2, it will prompt the user to enter a
        valid choice.
        """
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
        """A method for printing the total score of the players."""
        print('Scores:\n'
              f'{self.player_one.name}: '
              f'{self.player_one.total_score}\n'
              f'{self.player_two.name}: '
              f'{self.player_two.total_score}\n')
        return

    def show_histogram(self):
        """Calls the show_histogram method from the Histogram class."""
        self.histogram.show_histogram()
        return
