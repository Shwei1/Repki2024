from constants import *
from random import randint
from ship import Ship
from new_board import Board
from new_manager import *


class Game:
    def __init__(self):
        self.bot_board = VIRTUAL_BOT
        self.fleet = BOT_FLEET

    def bot_ships(self, size):
        '''
        генерує корабель за заданим розміром i розставляє на дошці
        '''
        
        while True:
            start_pos = (randint(0, 9), randint(0, 9))
            orient = randint(0, 1)
            try:
                ship = Ship(start_pos, orient, size)
                self.bot_board = Board(self.bot_board).add_ship(ship)
                self.fleet[size] -= 1
                break
            except AssertionError:
                pass


if __name__ == '__main__':
    Game().bot_ships(4)
    Game().bot_ships(3)
    Game().bot_ships(3)
    for x in VIRTUAL_BOT:
        print(x)
