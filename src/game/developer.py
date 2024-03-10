import tools


class Developer:
    """
    A class for the developer. It has a password and a Tools object.
    Currently, the only thing the developer can do is give 100 points to
    the player.
    """

    def __init__(self):
        """
        Constructor for Developer class. Sets the password and creates
        a Tools object.
        """
        self.password = "asd"
        self.tools = tools.Tools()

    def developer_menu(self, player):
        """
        A method for the developer menu. It prompts the user to enter a
        password. If the password is correct, it will display the developer
        menu. If the password is incorrect, it will return to the main menu.

        If the user enters 1, it will give 100 points to the player.
        If the user enters 2, it will go back to the main menu.
        """
        self.tools.clear_screen()
        password_try = input("Enter password: ")
        self.tools.clear_screen()
        if password_try == self.password:
            print("Menu: \n", "1. Give 100 points to player\n", "2. Go back\n")
            choice = int(input(">>> "))
            if choice == 1:
                player.total_score = 100
                print(f"{player.name} now has 100 points")
                self.tools.enter_to_continue()
                self.tools.clear_screen()
            else:
                self.tools.clear_screen()
                return
