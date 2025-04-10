# File: minimax_strategy.py
from src.game_board import GameBoard
from src.move_strategy import MoveStrategy
from src.player import Player


class MinimaxStrategy(MoveStrategy):
    """Implements the Minimax algorithm for optimal AI moves."""

    def find_best_move(self, board: GameBoard, player: Player) -> tuple[int, int]:
        """
        Find the optimal move using Minimax.

        Parameters:
            board (GameBoard): The game board instance.
            player (Player): The AI player instance.

        Returns:
            tuple[int, int]: (row, col) of the best move.
        """
        pass

    def minimax(self, board: GameBoard, depth: int, is_maximizing: bool,
                player: Player, opponent: Player) -> int:
        """
        Recursively evaluate board states with Minimax.

        Parameters:
            board (GameBoard): Current board state.
            depth (int): Depth in the game tree (moves made).
            is_maximizing (bool): True if maximizing (X), False if minimizing (O).
            player (Player): The AI player (maximizing).
            opponent (Player): The human player (minimizing).

        Returns:
            int: Score of the board state.
        """
        pass