# File: gui.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

from src.game_controller import GameController


class TicTacToeGUI(QMainWindow):
    """PyQt6-based GUI for Tic-Tac-Toe."""

    def __init__(self, controller: GameController):
        """
        Initialize the GUI with a controller.

        Parameters:
            controller (GameController): The game controller instance.
        """
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 350)  # Fixed window size

    def setup_ui(self) -> None:
        """Create the 3x3 button grid and status label."""
        pass

    def button_click(self, row: int, col: int) -> None:
        """
        Handle button clicks for human moves.

        Parameters:
            row (int): Row index (0-2).
            col (int): Column index (0-2).
        """
        pass

    def update_board(self) -> None:
        """Update the GUI to reflect the current board state."""
        pass

    def show_result(self, message: str) -> None:
        """
        Display the game result.

        Parameters:
            message (str): Result message (e.g., 'X wins!').
        """
        pass

    def run(self) -> None:
        """Start the GUI application."""
        app = QApplication(sys.argv)
        self.setup_ui()
        self.show()
        sys.exit(app.exec())