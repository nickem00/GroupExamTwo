"""
The exceptions.py file contains custom exceptions for the game.
"""


class GameExitException(Exception):
    pass


class RolledAOneException(Exception):
    pass


class ComputerWonException(Exception):
    pass
