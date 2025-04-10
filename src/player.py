# File: player.py
from abc import ABC, abstractmethod
from typing import Annotated

from src.game_board import GameBoard


class Player(ABC):
    """Parent base class for players in the game."""
    symbol: Annotated[str, "Player symbol: 'X' or 'O'"]

    def __init__(self, symbol: str):
        """
        Initialize a player with a symbol.

        Parameters:
            symbol (str): 'X' or 'O'.
        """
        self.symbol = symbol


# if __name__ == "__main__":
#     help(Player)

