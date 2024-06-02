from constants import *
from ship import Ship
from new_manager import *


class Board:

    def __init__(self, map):
        '''
        Відтворює ігрову дошку гравця i бота
        '''
        self.map = map
        self.ships = [0, 0, 0, 0]
        self.fleet = {1: 0, 2: 0, 3: 0, 4: 0}

    def add_ship(self, ship: Ship):
        '''
        додає корабель на ігрову дошку,
        викликає метод, який заповнює периметр
        '''
        ship_coordinates = ship.get_body()
        if check_area(ship, self.map):
            for coordinate_set in ship_coordinates:
                x, y = coordinate_set[0], coordinate_set[1]
                self.map[x][y] = 'x'
                self.fleet[ship.size] += 1
                self.ships.append(ship)
        else:
            raise AssertionError("Ставити тут корабель заборонено!")

        self.points(ship)

    def points(self, ship: Ship):
        '''
        позначає на дошці заборонені коорди
        '''
        perimeter = ship.get_perimeter()
        for coord in perimeter:
            x, y = coord[0], coord[1]
            if self.map[x][y] == 0 or self.map[x][y] == '.':
                self.map[x][y] = '.'
            else:
                raise AssertionError("Ставити тут корабель заборонено!")


if __name__ == '__main__':

    Board(FIELD).add_ship(Ship((6, 7), 0, 4))
    Board(FIELD).add_ship(Ship((5, 7), 0, 4))

    for x in FIELD:
        print(x)
