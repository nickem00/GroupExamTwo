import intelligence
import player
import settingsClass
import rules
import developer
import histogram
import tools


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
