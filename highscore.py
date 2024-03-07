import player
class Highscore():

    def __init__(self):
        pass

    def new_highscore(self, player_name, player_score, filename):
        current_highscore = self.highscore_tracker(filename)


    def highscore_tracker(self, filename):

        with open(filename, "r") as highscore_file:
            highscore_dictionary = {}
            for line in highscore_file:
                player, highscore = line.rstrip("\n").split(":")
                highscore_dictionary[player] = int(highscore)
            return highscore_dictionary

    def save_new_highscore(self, player_name, player_score, filename):
         pass
