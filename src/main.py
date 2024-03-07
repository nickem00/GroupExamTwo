import playerVsComputer
import playerVsPlayer
import tools

'''
Main method for the game.
Contains the Start Menu and the game loop.
'''


def main():
    tools.Tools().clear_screen()
    print("Welcome to the Game!")

    choice = input('Please choose an option:\n'
                   '1. Player vs Computer\n'
                   '2. Player vs Player\n'
                   '0. Exit\n'
                   'Enter your choice (1, 2, or 0 to exit): ')

    if choice == "1":
        game_controller = playerVsComputer.PlayerVsComputer()
        game_controller.game_startup()
    elif choice == "2":
        game_controller = playerVsPlayer.PlayerVsPlayer()
        game_controller.game_startup()
        pass
    elif choice == "0":
        print("Exiting the game. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
    main()


if __name__ == "__main__":
    main()

# teststestes
