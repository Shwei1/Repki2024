from new_board import Board
from window import window
import tkinter as tk
from constants import *


class VisualBoard:
    def __init__(self, board: Board):
        self.board = board

    def create_canvas(self):
        field_width = len(FIELD[0])
        field_height = len(FIELD)
        self.window.config(
            width=field_width,
            height=field_height
        )

        self.window.resizable(
            width=True,
            height=True
        )

        canvas = tk.Canvas(
            self.window,
            width=600,
            height=300,
            bg='gray'
        )
        canvas.pack(fill=tk.BOTH, expand=True)

        return canvas

    def draw_field(self):
        """
        Малює ігрову дошку
        """
        width = len(FIELD[0])
        height = len(FIELD)

        color = ''
        self.canvas.delete("all")

        for i in range(height):
            for j in range(width):

                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

                if self.map[i][j] == 0:
                    color = "white"
                if self.map[i][j] > 0:
                    color = "blue"
                if self.map[i][j] == -1:
                    color = "gray"
                if self.map[i][j] == -2:
                    color = "red"
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )
        self.canvas.pack()
        return self.canvas

