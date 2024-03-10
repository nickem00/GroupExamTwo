class SettingsClass:
    """
    The SettingsClass class is used to change the difficulty level of the game.
    """
    def __init__(self):
        """
        Initializes the SettingsClass object.
        """
        pass

    def change_difficulty(self):
        """
        Prompts user to select new difficulty level.
        Returns the new difficulty level if it is valid.
        """
        new_difficulty = int(input('Please select new difficulty:\n'
                                   '1. Easy\n'
                                   '2. Medium\n'
                                   '3. Hard\n'
                                   '>>> '))
        if 1 <= new_difficulty <= 3:
            return new_difficulty
