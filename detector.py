from board import Board
from constants import *
from window import window



def on_click(event):

    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    print(f"Clicked on cell: {col}, {row}")


if __name__ == "__main__":

    boardq = Board()
    boardq.draw_field().bind("<Button-1>", on_click)
    boardq.draw_field()
    window.mainloop()





