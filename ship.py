from constants import *


class Ship:

    def __init__(self, start_pos: tuple, orient: int, size: int):

        '''
        Корабель має розмір та список позицій на полі.

        :param start_pos: початкова позиція, де (x, y) - координати матриці
        :param orient: напрямок корабля, HORIZONTAL = 0, VERTICAL = 1
        :param size: розмір (к-сть клітинок; 1, 2, 3 or 4)
        '''

        self.start_pos = start_pos
        self.orient = orient
        self.size = size

    def get_body(self):

        '''
        визначає координати, які займає один корабель
        '''
        if self.orient == HORIZONTAL:
            if self.size + self.start_pos[1] <= 10:

                for i in range(self.size):
                    yield (self.start_pos[0], self.start_pos[1] + i)
            else:
                raise AssertionError('Корабель виходить за межі дошки')

        else:
            if self.size + self.start_pos[0] <= 10:
                for i in range(self.size):
                    yield (self.start_pos[0] + i, self.start_pos[1])
            else:
                raise AssertionError('Корабель виходить за межі дошки')

    def get_area(self):
        """"
        визначає заборонені клітинки по периметру корабля
        """""

        if self.orient == HORIZONTAL:
            x1, x2 = self.start_pos[0] - 1, self.start_pos[0] + 1
            y1, y2 = self.start_pos[1] - 1, self.start_pos[1] + self.size
        else:
            x1, x2 = self.start_pos[0] - 1, self.start_pos[0] + self.size
            y1, y2 = self.start_pos[1] - 1, self.start_pos[1] + 1

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                yield (i, j)


if __name__ == '__main__':
    for x in Ship((9, 0), 1, 4).get_body():
        print(x)
raise AssertionError('Корабель виходить за межі дошки')