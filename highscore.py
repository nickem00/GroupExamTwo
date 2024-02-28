class Highscore():

    def __init__(self):
        self.player_highscore = []

    def add_highscore(self, score):
        self.player_highscore.append(score)
        self.player_highscore.sort(reverse=True)

    def print_highscore(self):
        if self.player_highscore:
            print(f'''Your current Highscore is {self.player_highscore}
                  in one round! ''')
        else:
            print('No current Highscores. Time to play!')

    def print_top_scores(self, top=5):
        for i in range(0, top):
            print(f'{i+1}. {self.player_highscore[i]}')
