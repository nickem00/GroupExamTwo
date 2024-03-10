# conftest.py
import sys
import os


def pytest_configure():
    """
    This function is called when pytest starts.
    It was the only way I could make both the game and the tests work
    at the same time.
    """
    current_dir = os.path.dirname(__file__)
    game_dir = os.path.join(current_dir, '..')
    sys.path.insert(0, game_dir)
