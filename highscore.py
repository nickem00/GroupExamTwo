import player

class Highscore():

    def __init__(self):
        self.player_highscore = {}

    def add_highscore(self, score):
        self.player_highscore.append(score)
        self.player_highscore.sort(reverse=True)

    def save_player_highscore(self, filename):
        with open(filename, "a") as highscore_file:
            for player, highscore in self.player_highscore.items():
                highscore_file.write(f"{player}: {highscore}\n")

    def print_highscore(self, filename):
        with open(filename, "r") as open_highscore_file:
            for line in open_highscore_file:
                player, 

