from constants import *


class Ship:
    def __init__(self, start_pos: tuple, orient: int, size: int):
        self.start_pos = start_pos
        self.orient = orient
        self.size = size
        self.is_bots = False

    def get_body(self):
        body = []
        if self.orient == HORIZONTAL:
            if self.size + self.start_pos[1] <= 10:
                for i in range(self.size):
                    body.append((self.start_pos[0], self.start_pos[1] + i))
            elif not self.is_bots:
                raise AssertionError('Корабель виходить за межі дошки')
        else:
            if self.size + self.start_pos[0] <= 10:
                for i in range(self.size):
                    body.append((self.start_pos[0] + i, self.start_pos[1]))
            elif not self.is_bots:
                raise AssertionError('Корабель виходить за межі дошки')
        return body

    def get_area(self):
        area = set()
        body = self.get_body()
        
        for (x, y) in body:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in body:
                        area.add((nx, ny))
        return area
