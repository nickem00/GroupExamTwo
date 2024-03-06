import tools


class Developer:
    def __init__(self):
        self.password = 'asd'
        self.tools = tools.Tools()

    def developer_menu(self, player):
        self.tools.clear_screen()
        password_try = input('Enter password: ')
        self.tools.clear_screen()
        if password_try == self.password:
            print('Menu: \n',
                  '1. Give 100 points to player\n',
                  '2. Go back\n')
            choice = int(input('>>> '))
            if choice == 1:
                player.total_score = 100
                print(f'{player.name} now has 100 points')
                self.tools.enter_to_continue()
                self.tools.clear_screen()
            else:
                self.tools.clear_screen()
                return
