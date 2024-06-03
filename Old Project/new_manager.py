from ship import Ship

def check_area(ship: Ship, map):
    """
    Перевірка наявності кораблів в околі заданого корабля
    """
    fahrwasser = ship.get_body()   # змінна з координатами в околі корабля
    for coordinate_set in fahrwasser:
        x, y = coordinate_set[0], coordinate_set[1]
        if map[x][y] != 0:
            return False
    else:
        return True
