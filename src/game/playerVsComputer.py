# import os
import player
import time
import tools
import intelligence
import rules
import settingsClass
from exceptions import (GameExitException,
                        RolledAOneException,
                        ComputerWonException)
import developer
import histogram
import highscore


class PlayerVsComputer:
    """
    This is the PlayerVsComputer class. It is one of the main classes
    for the game. It's for the Player vs Computer mode. It contains
    the game loop and the game startup. It also contains methods for
    showing the rules, changing the name of the player, and changing
    the difficulty of the game.
    """

    def __init__(self):
        """
        The constructor for the PlayerVsComputer class. It initializes
        the computer_player and human_player to None and creates different
        objects used in the game.
        """
        self.computer_player = intelligence.Intelligence()
        self.human_player = None
        self.tools = tools.Tools()
        self.difficulty = 1
        self.settings = settingsClass.SettingsClass()
        self.all_rules = rules.Rules()
        self.intelligence = intelligence.Intelligence()
        self.developer = developer.Developer()
        self.histogram = histogram.Histogram()
        self.highscores = highscore.Highscore()

    def game_startup(self):
        """
        The method for the game startup (Main menu). If there are no current
        human player, it prompts the user to enter the name of the player.
        The game will continue to run until the user chooses to exit the game.
        It also has an option to show the rules, highscores, and change the
        name of the player.
        """
        self.tools.clear_screen()
        print("Welcome to PIG Dice Game!")
        if not self.human_player:
            self.human_player = player.Player(input("Please enter "
                                                    "your name >> "))

        main_menu_options = {
            "1": ("Start Game", self.start_game),
            "2": ("Show Rules", self.show_rules),
            "3": ("Change Name", self.change_name),
            "4": ("Show Highscores", self.highscores.display_highscores),
            "5": ("Exit Game", None),
        }

        while True:
            self.print_main_menu(main_menu_options)
            try:
                choice = int(input(">>> "))
            except ValueError:

                print("Please enter a valid choice! Error: Not a number")
                time.sleep(2)
                continue

            if 1 <= choice <= 5:
                if choice == 5:
                    self.tools.close_game()
                else:
                    main_menu_options[str(choice)][1]()
            else:
                print("Please enter a valid choice!")

    def show_rules(self):
        """A small method for showing the rules of the game."""
        self.all_rules.show_rules()

    def change_name(self):
        """A method for changing the name of the human player."""
        self.human_player.set_name(input("Please enter new name >> "))

    def print_main_menu(self, main_menu_options):
        """A method for printing the main menu of the game."""
        print()
        print(f"Welcome {self.human_player.name}")
        for key in main_menu_options:
            print(f"{key}. {main_menu_options[key][0]}")

    def print_game_menu(self, game_menu_options):
        """A method for printing the game menu of the game."""
        print()
        for key in game_menu_options:
            print(f"{key}. {game_menu_options[key][0]}")

    def start_game(self):
        """
        A method for starting the game. It contains the game loop.
        Uses modulo to switch between the human player and the computer
        player. The game loop will continue until the user chooses to
        exit the game or either the human player or the computer player
        wins.
        """
        game_menu_options = {
            "1": ("Roll die", self.human_player.roll_die),
            "2": ("Hold", self.human_player.hold),
            "3": ("Change Difficulty", self.change_difficulty),
            "4": ("Exit game (Points reset)", None),
            " ": ("-------------------------", None),
            "5": ("Show Histogram", self.histogram.show_histogram),
            "6": ("Dev-Options", self.developer.developer_menu),
        }

        rounds = 0
        while True:
            try:
                if rounds % 2 == 0:
                    self.human_players_turn(rounds, game_menu_options)
                    rounds += 1
                else:
                    self.tools.clear_screen()
                    print("Computer players turn!")
                    self.computer_players_turn()
                    rounds += 1
            except (GameExitException, ComputerWonException):
                break

    def human_players_turn(self, rounds, game_menu_options):
        """
        A method for the human players turn. It runs until the user
        chooses to hold or rolls a 1. It also prints the game menu
        and prompts the user to choose an option from the game menu.
        These are the options in the game menu:
        1. Roll die
        2. Hold
        3. Change Difficulty
        4. Exit game (Points reset)
        5. Show Histogram
        6. Dev-Options
        """
        if rounds == 0:
            self.tools.clear_screen()
            print(f"You start {self.human_player.name}!")

        while True:
            self.print_game_menu(game_menu_options)
            try:
                choice = int(input(">>> "))
            except ValueError:
                print("Please enter a valid choice! Error: Not a number")
                time.sleep(2)
                continue

            if 1 <= choice <= 6:
                if choice == 4:
                    print("Exiting game..")
                    self.human_player.total_score = 0
                    raise GameExitException
                elif choice == 1:
                    try:
                        current_roll = (game_menu_options
                                        [str(choice)][1](self.histogram))
                        self.tools.clear_screen()
                        print(f"You rolled a {current_roll}")
                    except RolledAOneException:
                        print("\nYou rolled a 1! Your turn is over.")
                        input("Press enter to continue...")
                        break
                elif choice == 2:
                    game_menu_options[str(choice)][1](self.highscores)
                    self.tools.clear_screen()
                    if self.human_player.is_winning(100):
                        print(
                            f"***Congratulations {self.human_player.name}!"
                            "You won!***"
                        )
                        self.tools.enter_to_continue()
                        break
                    else:
                        print(
                            "You held! Your total score is "
                            f"now {self.human_player.total_score}"
                        )
                        print("-----------------------------------")
                        self.print_points()
                        self.tools.enter_to_continue()
                        break
                elif choice == 5:
                    game_menu_options[str(choice)][1]()
                elif choice == 6:
                    self.developer.developer_menu(self.human_player)
                else:
                    game_menu_options[str(choice)][1]()
            else:
                print("Please enter a valid choice")

    def computer_players_turn(self):
        """
        A method for the computer players turn. The computer players logic
        is based on the difficulty of the game, and can be found
        in the intelligence class. After the computer player has used the
        start_round method, it checks if the computer player is winning.
        Else, it prints the scores and goes to the next round.
        """
        self.computer_player.start_round(self.difficulty, self.histogram)
        if self.computer_player.is_winning(100):
            print("The computer won!")
            self.tools.enter_to_continue()
            raise ComputerWonException
        self.print_points()
        self.tools.enter_to_continue()

    def change_difficulty(self):
        """
        A method for changing the difficulty of the game.
        If the user selects the same difficulty, it prints a message
        saying so. If the user selects a new difficulty, it prints a
        message saying so.
        """
        new_difficulty = self.settings.change_difficulty()
        if new_difficulty == self.difficulty:
            print("You selected the same difficulty.")
        else:
            self.difficulty = new_difficulty
            print("You selected a new difficulty!")

    def print_points(self):
        """
        A method for printing the scores of the human player and the
        computer player. It uses the total_score attribute from the
        human_player and computer_player objects.
        """
        print(
            "Scores:\n"
            f"You: {self.human_player.total_score}\n"
            f"Computer: {self.computer_player.total_score}\n"
        )
