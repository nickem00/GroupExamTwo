# Pig Dice Game

This is a game developed in Python using object-oriented programming principles. The game supports player vs computer and player vs player modes.

## Game Structure

The game is structured into several Python files each serving a different purpose:

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

1. Run `main.py` to start the game.
2. Choose between 'Player vs Computer' and 'Player vs Player' modes.
3. Follow the on-screen instructions to play the game.

## Game Menu Options

In the game, you have several options:

1. Roll: Roll the dice.
2. Hold: Hold your current score.
3. Show Rules: Display the game rules.
4. Change Name: Change the player's name.
5. Show Histogram: Display a histogram of scores.
6. Exit game (Points Reset): Exit the game. Note that this will reset your points.
7. Developer Menu: Access the developer menu for additional options.

## How to ownload and use the code

1. Download the ZIP-file that contains the code through this link: *Insert link*
2. Extract the ZIP-file to any location on your computer.
3. Open a Python-compatible editor.
4. Open the folder as a project.
5. You can now edit the code as you see fit and/or play the game as described in the "How to play" section of this README.md file.
   
# How to run tests and generate coverage report

We have implemented a test suite to ensure the codes reliability and effectievness. This section will show you how to run the complete test and generate a coverage report: 

1. **Note**: Make sure you have a terminal application installed on your system to execute the below commands. If you do NOT, feel free to install any terminal application. Follow this link to install Git Bash:*https://git-scm.com/downloads*

2. **Install Required Packages**: To ensure that you will be able to run the tests you have to have the necessary packages installed. You can intall them using this command in the terminal:

    `pip install -r requirements.txt`

3. **Run Tests**: To run the complete test suite, execute the below command in the terminal:

    `pytest`

4. **Generate Coverage Report**: To generate a coverage report for the test, execute the below command in the  terminal:

    `coverage run -m pytest`

5. **Generate an HTML Coverage Report**: To generate an HTML coverage report for the test, execute the below command in the  terminal: 

    `coverage html`

This will generate an HTML report in the "htmlcov" directory. To open the report you can open the "index.html" file in your web browser.


Enjoy the game!