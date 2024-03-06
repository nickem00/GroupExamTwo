import playerVsComputer
# import Dice
# import player


def main():
    # print("Welcome to the Game!")

    # choice = input('Please choose an option:\n'
    #                '1. Player vs Computer\n'
    #                '2. Player vs Player\n'
    #                'Enter your choice (1 or 2): ')

    # if choice == "1":
    #     game_controller = playerVsComputer.Game()
    #     game_controller.game_startup()
    # elif choice == "2":
    #     # Add code for player vs player game here
    #     pass
    # else:
    #     print("Invalid choice. Please try again.")
    game_controller = playerVsComputer.PlayerVsComputer()
    game_controller.game_startup()


if __name__ == "__main__":
    main()

# teststestes
