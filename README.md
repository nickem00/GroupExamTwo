# Pig Dice Game

This is a game developed in Python using object-oriented programming principles. The game supports player vs computer and player vs player modes.

## Game Structure

The game is structured into several Python files, each serving a different purpose:

- `main.py`: This is the entry point of the game. It contains the main method for the game and the game loop.
- `playerVsComputer.py`: This file contains the logic for the game mode where a player plays against the computer.
- `playerVsPlayer.py`: This file contains the logic for the game mode where a player plays against another player.
- `tools.py`: This file contains various utility functions used across the game.
- `settingsClass.py`: This file contains a class for managing game settings.
- `rules.py`: This file contains the rules of the game.
- `developer.py`: This file contains developer-specific functionalities.
- `histogram.py`: This file is used for generating histograms related to the game.
- `intelligence.py`: This file is used for managing the game's AI when playing in player vs computer mode.
- `exceptions.py`: This file contains custom exceptions used in the game.

## Implementation of AI (Intelligence)

The `Intelligence` class in the `intelligence.py` file controls the actions of the computer player in the game. Here's how it is implemented:

- The `start_round` method initiates a round based on the chosen difficulty level.
- The `easy`, `medium`, and `hard` methods determine the number of dice rolls the computer player makes based on the difficulty level.
- The `roll_die` method simulates rolling the dice for the computer player and calculates the round score.
- The `hold` method determines when the computer player decides to hold its current score.
- The `is_winning` method checks if the computer player has reached the winning score.

## How to Play

1. Open a command prompt or terminal application.
2. Navigate to the `src/game` folder.
3. Run `main.py` to start the game.
4. Choose between 'Player vs Computer' and 'Player vs Player' modes.
5. Follow the on-screen instructions to play the game.

## Game Menu Options

Depending on the game mode chosen, the game menu will display different options:

- **Player vs Computer Mode**:
    - **Start Game**: This option starts the game.
    - **Show Rules**: This option displays the rules of the game.
    - **Change Name**: This option allows you to change the name of the player.
    - **Show Highscores**: This option displays the high scores of the game.
    - **Exit Game**: This option exits the game.

- **Player vs Player Mode**:
    - **Start Game**: This option starts the game.
    - **Show Rules**: This option displays the rules of the game.
    - **Show Highscores**: This option displays the high scores of the game.
    - **Exit Game**: This option exits the game.

## How to Download and Use the Code

1. Clone the repository by running the following command in your terminal:

    ```bash
    git clone https://github.com/nickem00/GroupExamTwo.git

## How to Run Tests and Generate Coverage Report

We have implemented a test suite to ensure the code's reliability and effectiveness. This section will show you how to run the complete test and generate a coverage report:

2. **Install Make**: Make is a build automation tool that simplifies the process of running commands. If you don't have Make installed, you need to install it.

3. **Create and Activate a Virtual Environment**: It is recommended to create and activate a virtual environment before running the tests. This isolates the project's dependencies from your system's Python installation. You can create and activate a virtual environment using the following commands in the terminal:

    ```bash
    python -m venv .venv
    source .venv/Scripts/activate
    ```

4. **Install Required Packages**: To ensure that you will be able to run the tests, you have to have the necessary packages installed. You can install them using this command in the terminal:

    ```bash
    make install
    ```


5. **Run Tests**: To run the complete test suite, execute the below command in the terminal:

    ```bash
    make test
    ```

6. **Generate Coverage Report**: To generate a coverage report for the test, execute the below command in the terminal:

    ```bash
    coverage run -m pytest
    coverage report -m
    ```

7. **Generate an HTML Coverage Report**: To generate an HTML coverage report for the test, execute the below command in the terminal:

    ```bash
    make test
    ```

   This will generate an HTML report named index.html in the "doc" directory. To open the report, you can open the "index.html" file in your web browser.

8. **Generate UML Diagrams**: To generate UML diagrams for the game, execute the below command in the terminal:

    ```bash
    make uml
    ```

   This will generate UML diagrams in PlantUML format in the "doc/uml" directory. You can then copy the code and the paste it on this site: *https://www.planttext.com/* to generate the diagrams.

8. **Generate HTML Documentation**: To generate an HTML documentation page you can use the following command:
    ```bash
    make html
    ```
    This will create an index.html file in the `docs/_build` folder.\
    The `make html` command uses Sphinx to detect docstrings, to automaticly generate a HTML Documentation.

Enjoy the game!