"""
The Minimax algorithm evaluates all possible moves to find the optimal one. Here’s the mathematical equation to calculate the best score:

Score Calculation:
If the maximizing player (e.g., X) wins: score = 10 - depth
If the minimizing player (e.g., O) wins: score = -10 + depth
If it’s a draw: score = 0
Depth is the number of moves made so far, used to prioritize quicker wins or slower losses.
Minimax Pseudocode:
minimax(board, depth, is_maximizing, player, opponent):
    if game is over:
        return score based on winner or draw
    if is_maximizing:
        best_score = -infinity
        for each empty cell:
            make move for player
            score = minimax(board, depth + 1, false, player, opponent)
            undo move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = +infinity
        for each empty cell:
            make move for opponent
            score = minimax(board, depth + 1, true, player, opponent)
            undo move
            best_score = min(best_score, score)
        return best_score

The AI chooses the move with the highest score when maximizing (X) or the lowest score when minimizing (O).
"""

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