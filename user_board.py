from tkinter import *
from tkinter import messagebox
from board import Board
from ship import Ship
from constants import CELL_SIZE, FIELD, LEFT_CLICK, RIGHT_CLICK, FLEET
from random import randint


class UserBoard():
    def __init__(self, canvas: Canvas, game):
        self.canvas = canvas
        self.game = game
        self.board = Board(FIELD)
        self.canvas.bind(
            "<Button-1>", lambda event: self.on_click(event))
        self.canvas.bind(
            "<Button-3>", lambda event: self.on_click(event))
        self.draw_field()

    def check_hit(self, event: tuple) -> bool:
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
            # assert type(ship) == Ship
            ship_coords = []
            for coord_pair in ship.get_body():
                ship_coords.append(coord_pair)
            is_subset = all(
                item in self.board.clicked_coordinates for item in ship_coords)
            # print(f"criterion: {is_subset}")
            # print(f"ship coordinates: {ship_coords}")
            if is_subset:
                for (x, y) in ship.get_area():
                    if (x, y) not in ship.get_body():
                        self.board.field[x][y] = -1

    def on_click(self, event):
        self.board.is_bot = False
        row = event.x // CELL_SIZE
        col = event.y // CELL_SIZE

        if event.num == LEFT_CLICK:
            direction = 1
        elif event.num == RIGHT_CLICK:
            direction = 0

        ship_size = self.board.max_ship_size()
        if ship_size != 0:
            ship = Ship((col, row), direction, ship_size)
            self.board.add_ship(ship)
            self.draw_field()

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
            return "blue"
        elif value == -1:
            return "gray"
        elif value == -2:
            return "red"

    def empty_fleet(self) -> bool:
        return all(self.board.fleet[size] >= FLEET[size] for size in self.board.fleet)


    def fill_board(self):
        self.board.is_bot = True
        while not self.empty_fleet(): #     == False
            start_pos = (randint(0, 9), randint(0, 9))
            orient = randint(0, 1)
            size = self.board.max_ship_size()
            ship = Ship(start_pos, orient, size)
            ship.is_bots = True
            self.board.add_ship(ship)
        self.draw_field()

    def bot_move(self):
        while True:
            row = randint(0, 9)
            col = randint(0, 9)
            if (row, col) not in self.board.clicked_coordinates:
                self.board.clicked_coordinates.append((row, col))
                hit = self.check_hit((row, col))
                if hit:
                    self.check_submerged_ships()
                self.draw_field()
                if self.check_win():
                    messagebox.showinfo("Game Over", "Bot Wins!")
                if not hit:
                    self.game.switch_turn()
                    break

    def check_win(self):
        return all(col != 1 for row in self.board.field for col in row)
