from copy import deepcopy
from ship import Ship
from constants import FLEET


class Board:
    def __init__(self, field):
        self.field = deepcopy(field)
        # self.visual_field = deepcopy(field)
        # self.virtual_field = deepcopy(field)

        self.ships = []
        self.fleet = {1: 0, 2: 0, 3: 0, 4: 0}

        self.is_bot = False

        self.clicked_coordinates = []

    def add_ship(self, ship: Ship) -> None:
        ship_coordinates = ship.get_body()
        if self.check_area(ship):
            if self.check_fleet():
                for coordinate_set in ship_coordinates:
                    x, y = coordinate_set[0], coordinate_set[1]
                    self.field[x][y] = 1
                else:
                    self.ships.append(ship)
                    self.fleet[ship.size] += 1
            elif not self.is_bot: # == False
                raise AssertionError("Перевищено кількість доступних кораблів!")
        elif not self.is_bot: # == False
            raise AssertionError("Ставити тут корабель заборонено!")

    def check_area(self, ship: Ship) -> bool:
        fahrwasser = ship.get_area()   # змінна з координатами в околі корабля
        for coordinate_set in fahrwasser:
            x, y = coordinate_set[0], coordinate_set[1]
            if self.field[x][y] > 0:
                return False
        else:
            return True


    def check_fleet(self) -> bool | None:
        for i in range(1, 5):
            if self.fleet[i] >= FLEET[i]:
                return False
            else:
                return True
        pass

    def max_ship_size(self) -> int:
        sizes = [size for size in self.fleet if self.fleet[size] < FLEET[size]]
        sizes.append(0)
        return max(sizes)
