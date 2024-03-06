class SettingsClass:
    def __init__(self):
        pass

    def change_difficulty(self, difficulty):
        new_difficulty = int(input('Please select new difficulty:\n'
                                   '1. Easy\n'
                                   '2. Medium\n'
                                   '3. Hard\n'
                                   '>>> '))
        if 1 <= new_difficulty <= 3:
            return new_difficulty
