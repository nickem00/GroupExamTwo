import tools


class Highscore:
    """
    A class for handling highscores. It has methods for reading, displaying,
    checking, and saving highscores. It also has a method for sorting the
    highscores.
    """

    def __init__(self):
        """The constructor for the Highscore class. It sets the highscore file
        and creates a new tools object.
        """
        self.highscoreFile = "highscore.txt"
        self.tools = tools.Tools()

    def read_highscores(self):
        """A method for reading the highscores from the highscore file. It
        reads the highscores from the file and returns them as a dictionary.
        This method is used by the other methods in the class.
        """
        try:
            with open(self.highscoreFile, "r") as highscore_file:
                highscores = {}
                for line in highscore_file:
                    player, highscore = line.rstrip("\n").split(":")
                    highscores[player] = int(highscore)
                return highscores
        except FileNotFoundError:
            return {}

    def display_highscores(self):
        """A method for displaying the highscores. It reads the highscores
        and prints them to the screen. If there are no highscores, it will
        print that there are no highscores found.
        """
        self.tools.clear_screen()
        highscores = self.read_highscores()
        if highscores:
            print("Highscores:")
            print("-----------\n")
            i = 0
            for player, score in list(highscores.items())[:5]:
                i += 1
                print(f"{i}. {player}: {score}")
            print()
        else:
            print("No highscores found.")
        self.tools.enter_to_continue()

    def is_highscore(self, player_name, player_score):
        """
        A method for checking if the player has a highscore. It takes in the
        player name and score and checks if the player has a highscore. If
        the player has a highscore, it checks if the new score is higher
        than the old one. If the player does not have a highscore, the
        method will return True.
        """
        highscores = self.read_highscores()
        if player_name in highscores:
            if player_score > highscores[player_name]:
                return True
            else:
                return False
        else:
            return True

    def save_new_highscore(self, player_name, player_score):
        """
        A method for saving a new highscore. It takes in the player name
        and score, checks if the player already has a highscore,
        and if so, if the new score is higher than the old one.
        If the player has a highscore, the method will update the
        highscore if the new score is higher.
        If the player does not have a highscore, the method will add
        the player and score to the highscore list.

        The method will then sort the highscores and write them to the
        highscore file.
        """
        highscores = self.read_highscores()
        if player_name in highscores:
            if player_score > highscores[player_name]:
                highscores[player_name] = player_score
                print(
                    f"New highscore! ({player_score}) Your highest "
                    "score is now saved!"
                )
                self.tools.enter_to_continue()
            else:
                pass
        else:
            highscores[player_name] = player_score
            print("Congratulations! Your highest score is now saved!")
            self.tools.enter_to_continue()

        highscore_sorting = highscores.items()
        sorted_list = sorted(highscore_sorting,
                             key=lambda item: item[1],
                             reverse=True)
        sorted_highscores = dict(sorted_list)

        with open(self.highscoreFile, "w") as highscore_file:
            for player, score in sorted_highscores.items():
                highscore_file.write(f"{player}: {score}\n")
