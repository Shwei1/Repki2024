from constant import *


class Board:

    def __init__(self):

        '''
        Відтворює ігрову дошку, розміщує всі кораблі, перевіряє влучення,
        перевіряє можливість розташування кораблів

        :param size: розмір дошки (за замовчуванням)
        '''

        self.size = SIZE_BOARD
        self._ships = []

    def add_ship(self, ship):
        '''
        додає корабель на ігрову дошку
        '''
        pass

    def check_hit(self):
        '''
        перевіряє чи стоїть на заданих координатах корабель
        '''
        pass