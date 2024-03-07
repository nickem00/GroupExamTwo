from tools import Tools


class Rules:
    def __init__(self):
        self.tools = Tools()

    '''
    Method to show the rules of the game.
    '''
    def show_rules(self):
        self.tools.clear_screen()
        print('''Welcome to the PIG Dice Game!
        Here are the rules:
        1. The game is played by two players.
        A human player and a computer player.
        2. The game is turn-based. The human player goes first.
        3. The goal of the game is to reach 100 points.
        4. If a player rolls a 1, the player's turn ends and the player
        loses all points accumulated during the turn.
        5. If a player rolls a 2-6, the player can choose to roll again.
        6. If a player chooses to hold, the points accumulated during the
        turn are added to the player's total points.
        7. The computer player is set to easy difficulty by default.
        ''')
        self.tools.enter_to_continue()
        self.tools.clear_screen()
