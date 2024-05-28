from constants import *
from window import window
from field import field
import tkinter as tk
from ship import Ship
import copy
# from manager import *


class Board:
    def __init__(self):
        self.window = window
        self.canvas = self.create_canvas()
        self.map = copy.deepcopy(FIELD)

        '''
        Відтворює ігрову дошку, розміщує всі кораблі, перевіряє влучення,
        перевіряє можливість розташування кораблів

        :param size: розмір дошки (за замовчуванням)
        '''

        self.size = SIZE_BOARD
        self.ships = {1: 0, 2: 0, 3: 0, 4: 0}

    def create_canvas(self):
        """
        Створює канвас з ігровою дошкою
        """
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

    def map_bringer(self):
        return self.map

    def draw_field(self):
        """
        Малює ігрову дошку
        """
        width = len(FIELD[0])
        height = len(FIELD)

        color = ''

        for i in range(height):
            for j in range(width):

                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

                if self.map[i][j] == 0:
                    color = "white"
                if self.map[i][j] > 0:
                    color = "blue"
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )
        self.canvas.pack()
        return self.canvas

    def add_ship(self, ship: Ship):
        '''
        додає корабель на ігрову дошку
        '''
        ship_coordinates = ship.get_body()
        if check_area(ship):
            if check_fleet(self):
                for coordinate_set in ship_coordinates:
                    x, y = coordinate_set[0], coordinate_set[1]
                    self.map[x][y] = 1
                    self.ships[ship.size] += 1
            else:
                raise AssertionError("Перевищено кількість доступних кораблів!")
        else:
            raise AssertionError("Ставити тут корабель заборонено!")

    def check_hit(self, coords):
        '''
        перевіряє чи стоїть на заданих координатах корабель
        '''

def check_area(ship: Ship):
    """
    Перевірка наявності кораблів в околі заданого корабля
    """
    fahrwasser = ship.get_area()   # змінна з координатами в околі корабля
    for coordinate_set in fahrwasser:
        x, y = coordinate_set[0], coordinate_set[1]
        if field[x][y] > 0:
            return False
    else:
        return True


def fleet_dictionary_manager(dictionary):
    """
    Сюди, можливо, перенесеться блок коду, що оновлює словник з кораблями на заданому полі
    """
    ...
    pass


def check_fleet(board: Board):
    for i in range(1, 5):
        if board.ships[i] >= FLEET[i]:
            return False
        else:
            return True
    pass



if __name__ == "__main__":
    # board1 = Board()
    board2 = Board()
    #
    # board1.add_ship(Ship((0, 0), 1, 1))
    # board1.add_ship(Ship((2, 2), 1, 1))
    # board1.add_ship(Ship((4, 4), 1, 1))
    # board1.add_ship(Ship((6, 6), 1, 1))
    # # board1.add_ship(Ship((8, 8), 1, 1))
    # # board1.add_ship(Ship((9, 9), 0, 1))
    # board1.draw_field()

    board1.add_ship(Ship((0, 0), 1, 1))
    board1.add_ship(Ship((2, 2), 1, 1))
    board1.add_ship(Ship((4, 4), 1, 1))
    board1.add_ship(Ship((6, 6), 1, 1))
    #board1.add_ship(Ship((8, 8), 1, 1))
    # board1.add_ship(Ship((9, 9), 0, 1))
    # board2.draw_field()
    # window.mainloop()
    print(board1.ships)
    board2.draw_field()
    window.mainloop()
    # print(board1.ships)
    # print(board2.ships)
