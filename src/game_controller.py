# File: game_controller.py
from src.ai_player import AIPlayer
from src.game_board import GameBoard
from src.human_player import HumanPlayer


class GameController:
    """Controls game flow, alternating between players."""

    def __init__(self, human: HumanPlayer, ai: AIPlayer, board: GameBoard):
        """
        Initialize the game with players and a board.

        Parameters:
            human (HumanPlayer): The human player.
            ai (AIPlayer): The AI player.
            board (GameBoard): The game board instance.
        """
        self.human = human
        self.ai = ai
        self.board = board
        self.current_player = human

    def switch_player(self) -> None:
        """Switch the current player between human and AI."""
        pass

    def check_game_over(self) -> tuple[bool, str]:
        """
        Check if the game has ended.

        Returns:
            tuple[bool, str]: (is_over, result_message).
        """
        pass