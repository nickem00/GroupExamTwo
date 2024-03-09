# conftest.py
import sys
import os


def pytest_configure():
    current_dir = os.path.dirname(__file__)
    game_dir = os.path.join(current_dir, '..')
    sys.path.insert(0, game_dir)
