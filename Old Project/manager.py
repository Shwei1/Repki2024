from window import window
from constants import *
from ship import Ship
from field import field
from old_board import Board

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

def on_click(event):

    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    print(f"Clicked on cell: {col}, {row}")




if __name__ == "__main__":
    for k in Ship((0, 0), 1, 1).get_area():
        print(k)



