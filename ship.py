from constant import *


class Ship:

    def __init__(self, start_pos: tuple, orient: int, size: int):

        '''
        Корабель має розмір та список позицій на полі.

        :param start_pos: початкова позиція
        :param orient: напрямок корабля, HORIZONT = 0, VERTICAL = 1
        :param size: розмір (к-сть клітинок)
        '''

        self.start_pos = start_pos
        self.orien = orient
        self.size = size

    def get_body(self):

        '''
        розміщує корабель, маючи стартову позицію i розмір
        '''

        pass

    def get_area(self):
        '''
        визначає заборонені клітинки по периметру корабля
        '''

        pass