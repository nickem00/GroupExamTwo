class Developer:
    def __init__(self):
        self.password = 'asd'

    def developer_menu(self, player):
        password_try = input('Enter password: ')
        if password_try == self.password:
            print('Menu: \n',
                  '1. Give 100 points to player\n',
                  '2. Go back\n')
            choice = int(input('>>> '))
            if choice == 1:
                player.total_score = 100
                print(f'{player.name} now has 100 points')
            else:
                return
