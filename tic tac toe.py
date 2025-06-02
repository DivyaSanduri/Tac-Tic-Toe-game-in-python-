import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Helvetica", 32),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
