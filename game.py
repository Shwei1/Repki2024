from tkinter import *
from constants import FIELD
from user_board import UserBoard
from bot_board import BotBoard


class Game(Toplevel):
    def __init__(self, root: Tk, username: str):
        self.root = root
        self.root.title("SEA BATTLE")
        self.root.geometry("1200x700")

        self.user_turn = True

        # Configure the grid for the entire window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        Label(self.root, text=f"Welcome, {username}!",
              font="Verdana 30").grid(row=0, column=0, columnspan=3, pady=10)

        bot_canvas = self.create_canvas(1, 0)
        self.bot_board = BotBoard(bot_canvas, self)

        user_canvas = self.create_canvas(1, 2)
        self.user_board = UserBoard(user_canvas, self)

        reset_button = Button(self.root, text="Reset", width=20, height=3, command=self.reset)
        reset_button.grid(row=2, column=0, pady=10)

        play_button = Button(self.root, text="Play", width=20, height=3, command=self.play)
        play_button.grid(row=2, column=1, pady=10)

        randomize_button = Button(
            self.root, text="Randomize", width=20, height=3, command=self.randomize)
        randomize_button.grid(row=2, column=2, pady=10)

    def reset(self):
        # Clear existing canvases
        self.bot_board.canvas.delete("all")
        self.user_board.canvas.delete("all")
    
        # Recreate bot board
        bot_canvas = self.create_canvas(1, 0)
        self.bot_board = BotBoard(bot_canvas, self)

        # Recreate user board
        user_canvas = self.create_canvas(1, 2)
        self.user_board = UserBoard(user_canvas, self)

    def play(self):
        if self.user_board.empty_fleet() != 0:
            self.bot_board.fill_board()
        else:
            print("You need to place all ships!")

    def randomize(self):
        self.user_board.fill_board()

    def switch_turn(self):
        self.user_turn = not self.user_turn
        if not self.user_turn:
            self.user_board.bot_move()

    def create_canvas(self, row: int, col: int):
        field_width = len(FIELD[0])
        field_height = len(FIELD)
        self.root.config(
            width=field_width,
            height=field_height
        )

        self.root.resizable(
            width=True,
            height=True
        )

        canvas = Canvas(
            self.root,
            width=398,      # not 500, grey line
            height=398,     # not 500, grey line
            bg='gray'
        )
        canvas.grid(row=row, column=col, padx=10, pady=10)

        return canvas
