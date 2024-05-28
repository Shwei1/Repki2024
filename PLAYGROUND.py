import board
from board import Board
from ship import Ship
from detector import on_click
from window import window

if __name__ == "__main__":
    board1 = Board()
    board2 = Board()
    # board1.draw_field().bind("<Button-1>", on_click)
    board1.add_ship(Ship((0, 0), 1, 1))
    board1.add_ship(Ship((2, 2), 1, 1))
    board1.add_ship(Ship((4, 4), 1, 1))
    board1.add_ship(Ship((8, 5), 0, 4))
    # board1.add_ship(Ship((8, 8), 1, 1))
    # board1.add_ship(Ship((9, 9), 0, 1))
    board1.draw_field()
    board2.draw_field()
    window.mainloop()
    # print(board1.ships)
    # print(board2.ships)

