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
        >>> game.game_board[0][0] = "X"
        >>> game.game_board[0][1] = "O"
        >>> game.game_board[1][0] = "X"
        >>> game.game_board[1][1] = "O"
        >>> game.game_board[2][0] = "X"
        >>> game.game_board[2][1] = "O"
        >>> # Get any empty cells
        >>> print("\\nEmpty cells: ", end="")
        >>> print(game.get_empty_cells(), end="\\n\\n")
        >>> # Display the game board
        >>> game.display()

    """
    game_board = Annotated[List, "The GameBoard"]

    def __init__(self):
        """
        Initialize an empty 3x3 board as a 2D list.

        Example:
        =======
        >>> from src.game_board import GameBoard
        >>> game = GameBoard()
        >>> # Add X and O to the game board
        >>> game.game_board[0][0] = "X"
        >>> game.game_board[0][1] = "O"
        >>> game.game_board[1][0] = "X"
        >>> game.game_board[1][1] = "O"
        >>> game.game_board[2][0] = "X"
        >>> game.game_board[2][1] = "O"
        >>> # Get any empty cells
        >>> print("\\nEmpty cells: ", end="")
        >>> print(game.get_empty_cells(), end="\\n\\n")
        >>> # Display the game board
        >>> game.display()
"""
        # Initializes the board as a 3 by 3 2D list
        self.game_board = [["" for _ in range(3)] for _ in range(3)]

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
        # Captures an exception as a result of a user placing a symbol in a none empty
        try:
            # Convert symbol to uppercase for convention
            symbol = symbol.upper()
            # Raise an exception, and doesn't place a symbol if a cell is not empty
            if len(self.game_board[row][col]) != 0:
                # Displays an error message
                raise ValueError("This cell is not empty.")
            # Otherwise places the symbol in a cell if a cell is empty
            self.game_board[row][col] = symbol
            # Returns true
            return True, ""
        # Raises a ValueError if a human player places a symbol in a none empty cell
        except ValueError as e:
            # Return False and displays the Error message: "This cell is not empty."
            return False, e.args[0]

    def is_winner(self, symbol: str) -> bool:
        """
        Check if the given symbol has won (row, column, diagonal).
        Domains: rows, columns, diagonal (left --> right) and anti-diagonal (left <-- right)

        The gameboard (2D Array):
            [
            [X, X, 0]   # Row 1, Index 0, contains a list with 3 Columns
            [O, O, O]   # Row 2, Index 1, contains a list with 3 Columns
            [X, X, X]   # Row 3, Index 2, contains a list with 3 Columns
            ]

        Parameter:
            symbol (str): The player symbol, i.e "X" or "O"

        Returns:
            bool: True if the symbol wins, False otherwise.
        """
        # Symbol must always be uppercase, so make sure to change to uppercase
        symbol = symbol.upper()

        # Check if you have a row win and return before resetting the variable
        if self._row_win(symbol):
            return True

        # Check the rows and columns to see if we find a winning row
        if self._col_win(symbol):
            return True

        # Checks diagonal for a winner
        if self._diag_win(symbol):
            return True

        # Check the anti-diagonal for a winner
        if self._anti_diag_win(symbol):
            return True

        return False

    def _anti_diag_win(self, symbol: str):
        # Symbol must always be uppercase, so make sure to change to uppercase
        symbol = symbol.upper()
        # Capture the row and column sizes
        rows = len(self.game_board)
        cols = len(self.game_board[0]) - 1

        # This inner for loop checks each anti-diagonal for a winner
        for row in range(rows):
            print(f"({row},{cols}) => {self.game_board[row][cols]}")

            if self.game_board[row][cols] != symbol:
                print(f"Found a false: ({row}, {cols})")
                return False
            cols -= 1
        return True

    def _diag_win(self, symbol: str):
        # Symbol must always be uppercase, so make sure to change to uppercase
        symbol = symbol.upper()
        # Capture the gameboard size
        indexes = len(self.game_board)
        # Check the diagonal in a single pass
        for index in range(indexes):
            if self.game_board[index][index] != symbol:
                return False

        return True

    def _col_win(self, symbol: str):
        # Symbol must always be uppercase, so make sure to change to uppercase
        symbol = symbol.upper()
        # Capture the row and column sizes
        rows = len(self.game_board)
        cols = len(self.game_board[0])

        # Check the columns to see if we find a winning column
        for row in range(rows):
            # Set column win to true and check for a false state (a non-matching symbol)
            # Define sentinels
            col_win = True

            # This inner for loop checks each column for a winner
            print("\n\nChecking Columns: ")
            print(f"Rows: [0, 1, 2], Col: {row}")
            for col in range(cols):
                # Test the columns
                print(f"Col: {row}, Row: {col}")
                # print(f"{self.gameboard[col][row]}", end="\n")
                if self.game_board[col][row] != symbol:
                    col_win = False

            # Check if you have a column win and return before resetting the variable
            if col_win:
                return True

        return False

    def _row_win(self, symbol: str):
        # Symbol must always be uppercase, so make sure to change to uppercase
        symbol = symbol.upper()
        # Capture the row and column sizes
        rows = len(self.game_board)
        cols = len(self.game_board[0])

        # Check the rows to see if we find a winning row
        for row in range(rows):
            # Set row win to true and check for a false state (a non-matching symbol)
            # Define sentinels
            row_win = True

            # This inner for loop checks each row for a winner
            print("\nChecking Rows: ")
            print(f"Row: {row}, Cols: [0, 1, 2]")
            for col in range(cols):
                # Test rows
                print(f"Row: {row}, Col: {col}")
                # print(f"{self.gameboard[row][col]}", end= "")
                if self.game_board[row][col] != symbol:
                    row_win = False

            # Check if you have a row win and return before resetting the variable
            if row_win:
                return True

        return False

    def is_full(self) -> bool:
        """Check if the board is full (no empty spaces)."""
        # If there are 0 empty cells in the board return True
        if len(self.get_empty_cells()) == 0:
            return True
        # Else if there are empty cells return False
        else:
            return False

    def get_empty_cells(self) -> list[tuple[int, int]]:
        """
        Return a list of (row, col) tuples for empty cells.

        Returns:
            list[tuple[int, int]]: List of empty cell coordinates.
            example: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 0)]
        """
        # Empty tuple
        empty_cells = []
        # Iterates through the rows in self.gameboard
        for row in range(len(self.game_board)):
            # Iterates through the columns in self.gameboard
            for col in range(len(self.game_board[row])):
                # If a cell in self.gameboard is empty add it to the empty cell tuple
                if len(self.game_board[row][col]) == 0:
                    empty_cells.append((row, col))

        # Return the tuple containing a list of empty cells
        return empty_cells

    def display(self) -> None:
        """Print the board to the console for debugging."""
        print()
        for row in self.game_board:
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


