import playerVsComputer
import playerVsPlayer
import tools


def run_game():
    """
    A function to run the game. It will prompt the user to choose between
    Player vs Computer, Player vs Player, or Exit.
    """
    while True:
        tools.Tools().clear_screen()
        print("Welcome to the Game!")

        choice = input(
            "Please choose an option:\n"
            "1. Player vs Computer\n"
            "2. Player vs Player\n"
            "0. Exit\n"
            "Enter your choice (1, 2, or 0 to exit): "
        )

        if choice == "1":
            game_controller = playerVsComputer.PlayerVsComputer()
            game_controller.game_startup()
            break
        elif choice == "2":
            game_controller = playerVsPlayer.PlayerVsPlayer()
            game_controller.game_startup()
            break
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")
            tools.Tools().enter_to_continue()


def main():
    run_game()


if __name__ == "__main__":
    main()

# teststestes
