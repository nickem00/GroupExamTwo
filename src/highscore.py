import player


class Highscore():

    def __init__(self):
        self.highscore_file = "highscore.txt"

    def new_highscore(self, player_name, player_score, filename):
        highscores = self.highscore_tracker(filename)

        if not highscores:
            self.save_new_highscore(player_name, player_score, filename)
        
        else:
            current_highscoreholder = list(highscores.keys())[-1]
            current_highscoreholder_score = highscores[current_highscoreholder]

            if player_score > current_highscoreholder_score:
                self.save_new_highscore(player_name, player_score, filename)
            else:
                pass

    def highscore_tracker(self, highscore_file):
            try:
                with open(highscore_file, "r") as highscore_file:
                    highscore_dictionary = {}
                    for line in highscore_file:
                        player, highscore = line.rstrip("\n").split(":")
                        highscore_dictionary[player] = int(highscore)
                    return highscore_dictionary
            except FileNotFoundError:
                print("Error: File not found")
                return {}  

    def save_new_highscore(self, player_name, player_score):
        try:
            highscores = self.highscore_tracker(self.highscore_file)
            highscores[player_name] = player_score

            with open(self.highscore_file, "w") as highscore_file:
                for player, score in highscores.items():
                    highscore_file.write(f"{player}: {score}\n")
                
        except FileNotFoundError:
            print("Error: File not found")


    #This function displays the top 5 highscores from the highscore_file.
    def display_highscore(self, highscore_file):
        with open(highscore_file, "r") as top_scores:
            highscores = [line.strip() for line in top_scores]
            highscores_reversed = highscores[::-1]

            if highscores:
                print("--Highscore leaderboard--")
                count = 0
                for items in highscores_reversed:
                    name, scores = items.split(":")
                    print(f"{name}: {scores}")
                    count += 1
                    if count >= 5:
                        break            
            else:
                print("No highscores have been added")
            
