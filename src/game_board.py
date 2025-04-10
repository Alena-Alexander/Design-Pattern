# File: game_board.py
import email.message
from typing import Annotated, Union, List


class GameBoard:
    """
    Models the Tic-Tac-Toe 3x3 game board using a 2D array.
    Handles moves, win checks, and board state.

    Example:
    ========
        >>> from src.game_board import GameBoard
        >>> game = GameBoard()
        >>> # Add X and O to the game board
        >>> game.gameboard[0][0] = "X"
        >>> game.gameboard[0][1] = "O"
        >>> game.gameboard[1][0] = "X"
        >>> game.gameboard[1][1] = "O"
        >>> game.gameboard[2][0] = "X"
        >>> game.gameboard[2][1] = "O"
        >>> # Get any empty cells
        >>> print("\\nEmpty cells: ", end="")
        >>> print(game.get_empty_cells(), end="\\n\\n")
        >>> # Display the game board
        >>> game.display()

    """
    gameboard = Annotated[List, "The GameBoard"]

    def __init__(self):
        """
        Initialize an empty 3x3 board as a 2D list.

        Example:
        =======
        >>> from src.game_board import GameBoard
        >>> game = GameBoard()
        >>> # Add X and O to the game board
        >>> game.gameboard[0][0] = "X"
        >>> game.gameboard[0][1] = "O"
        >>> game.gameboard[1][0] = "X"
        >>> game.gameboard[1][1] = "O"
        >>> game.gameboard[2][0] = "X"
        >>> game.gameboard[2][1] = "O"
        >>> # Get any empty cells
        >>> print("\\nEmpty cells: ", end="")
        >>> print(game.get_empty_cells(), end="\\n\\n")
        >>> # Display the game board
        >>> game.display()
"""
        # Hint: Use [[' ' for _ in range(3)] for _ in range(3)] for an empty board
        self.gameboard = [["" for _ in range(3)] for _ in range(3)]

    def make_move(self, row: int, col: int, symbol: str) -> tuple[bool, str]:
        """
        Place a symbol (X or O) at the given position if valid.

        Parameters:
            row (int): Row index (0-2).
            col (int): Column index (0-2).
            symbol (str): Player symbol ('X' or 'O').

        Returns:
            bool: True if move was successful, False if invalid.
        """
        try:
            # Raise an exception if the index it not empty
            if len(self.gameboard[row][col]) != 0:
                raise ValueError("This cell is not empty.")
            # Otherwise place the symbol at that index
            self.gameboard[row][col] = symbol
            return True, ""
        except ValueError as e:
            return False, e.args[0]

    def is_winner(self, symbol: str) -> bool:
        """
        Check if the given symbol has won (row, column, diagonal).

        Parameters:
            symbol (str): Player symbol to check ('X' or 'O').

        Returns:
            bool: True if the symbol wins, False otherwise.
        """
        pass

    def is_full(self) -> bool:
        """Check if the board is full (no empty spaces)."""
        if self.get_empty_cells() == 0:
            return True
        else:
            return False

    def get_empty_cells(self) -> list[tuple[int, int]]:
        """
        Return a list of (row, col) tuples for empty cells.

        Returns:
            list[tuple[int, int]]: List of empty cell coordinates.
            example: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 0)]
        """
        empty_cells = []
        for row in range(len(self.gameboard)):
            for col in range(len(self.gameboard[row])):
                if len(self.gameboard[row][col]) == 0:
                    empty_cells.append((row, col))
        return empty_cells

    def display(self) -> None:
        """Print the board to the console for debugging."""

        for row in self.gameboard:
            # Newline sentinel used to parse and format the 3X3 2D array
            # so it is stacked 3X3.
            newline = 3
            # Starts a new row
            print("[ ", end="")
            # Iterate over each column
            for col in row:
                # Decrement newline
                newline -= 1
                # Print a value with no newline, leaves the cursor on the line
                print(col, end="")
                # Prints the vertical bar if newline is not 0 and leaves the cursor on the line
                if newline != 0:
                    print(" | ", end="")
                # Closes the row with a closing bracket and prints newline character when newline is 0
                if newline == 0:
                    print(" ]", end="\n")



# if __name__ == "__main__":
#     game = GameBoard()
#     # Add X and O to the game board
#     game.make_move(0, 1, "X")
#     game.make_move(1, 1, "O")
#     game.make_move(2, 1, "X")
#     game.make_move(0, 2, "O")
#     game.make_move(0, 0, "X")
#     result = game.make_move(0, 0, "O")
#     print(result[0])
#     print(result[1])
#     # Get any empty cells
#     print("\nEmpty cells: ", end="")
#     print(game.get_empty_cells(), end="\n\n")
#     # Display the game board
#     game.display()



