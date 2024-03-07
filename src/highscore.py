import player


class Highscore():

    def init(self):
        pass

    def new_highscore(self, player_name, player_score, filename):
        current_highscore = self.highscore_tracker(filename)

        if player_score > current_highscore:
            self.save_new_highscore(player_name, player_score, filename)
        else:
            pass

    def highscore_tracker(self, filename):
        with open(filename, "r") as highscore_file:
            highscore_dictionary = {}
            for line in highscore_file:
                player, highscore = line.rstrip("\n").split(":")
                highscore_dictionary[player] = int(highscore)
            return highscore_dictionary

    def save_new_highscore(self, player_name, player_score, filename):
        with open(filename, "w") as highscore_file:
            for player, score in highscore_file:
                highscore_file.write(f"{player} with a score of: {score}")
