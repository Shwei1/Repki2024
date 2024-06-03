from tkinter import *
from tkinter import messagebox
from board import Board
from ship import Ship
from constants import CELL_SIZE, FIELD, FLEET
from random import randint


class BotBoard():
    def __init__(self, canvas: Canvas, game):
        self.game = game
        self.canvas = canvas
        self.board = Board(FIELD)
        self.board.is_bot = True
        self.canvas.bind(
            "<Button-1>", lambda event: self.on_click(event))
        self.draw_field()

    def check_hit(self, event: tuple):
        x, y = event
        if self.board.field[x][y] == 1:
            self.board.field[x][y] = -2
            return True
        elif self.board.field[x][y] == 0:
            self.board.field[x][y] = -1
            return False
        else:
            print("You already shot here")
            return False

    def check_submerged_ships(self):
        for ship in self.board.ships:
            ship_coords = ship.get_body()
            if all(coord in self.board.clicked_coordinates for coord in ship_coords):
                for x, y in ship.get_area():
                    if (x, y) not in ship.get_body():
                        self.board.field[x][y] = -1

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if (row, col) not in self.board.clicked_coordinates:
            self.board.clicked_coordinates.append((row, col))
            hit = self.check_hit((row, col))
            if hit:
                self.check_submerged_ships()
            self.draw_field()
            if self.check_win():
                    messagebox.showinfo("Game Over", "User Wins!")
            if not hit:
                print("Switch to Bot")
                self.game.switch_turn()
        else:
            pass

    def draw_field(self):
        width = len(FIELD[0])
        height = len(FIELD)
        for i in range(height):
            for j in range(width):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                color = self.get_color(self.board.field[i][j])
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
        return self.canvas
    
    def get_color(self, value) -> str:
        if value == 0:
            return "white"
        elif value > 0:
            return "white"
        elif value == -1:
            return "gray"
        elif value == -2:
            return "red"
    
    def empty_fleet(self) -> bool:
        return [size for size in self.board.fleet if self.board.fleet[size] < FLEET[size]] == []

    def fill_board(self):
        while not self.empty_fleet(): #     == False
            start_pos = (randint(0, 9), randint(0, 9))
            orient = randint(0, 1)
            size = self.board.max_ship_size()
            ship = Ship(start_pos, orient, size)
            ship.is_bots = True
            self.board.add_ship(ship)
        self.draw_field()

    def check_win(self):
        return all(col != 1 for row in self.board.field for col in row)
