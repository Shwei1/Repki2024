from constants import *
from random import randint
from ship import Ship


def gen_ships(size):
    '''
    генерує стартову позицію i орієнтацію для ycix кораблів

    :param size: розмір корабля
    :returns: список ycix клітинок, які займає корабель
    '''

    start_pos = (randint(0, 9), randint(0, 9))
    orient = randint(0, 1)
    ship_coords = Ship(start_pos, orient, size).get_body()
    for x in ship_coords:
        yield x

def gen_shot():
    '''перший постріл'''

    return (randint(0, 9), randint(0, 9))




