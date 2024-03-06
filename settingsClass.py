class SettingsClass:
    def __init__(self):
        pass

    '''
    Method for changing the difficulty of the game.
    Returns the new difficulty level as an integer to be changed in the
    playerVsComputer class.
    '''
    def change_difficulty(self):
        new_difficulty = int(input('Please select new difficulty:\n'
                                   '1. Easy\n'
                                   '2. Medium\n'
                                   '3. Hard\n'
                                   '>>> '))
        if 1 <= new_difficulty <= 3:
            return new_difficulty
