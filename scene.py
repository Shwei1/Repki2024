from window import window
from tkinter import *

class SeaBattleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SEA BATTLE")
        self.create_main_window()

    def create_main_window(self):
        c = Canvas(self.root, width=750, height=700)
        c.pack()

        c.create_text(370, 120,
                      text="SEA BATTLE",
                      justify=CENTER,
                      font="Verdana 50")
        # прямокутник шоб красіво
        c.create_rectangle(175, 60, 580, 185)
        # текст тіпа прівєтсвіє
        c.create_text(380, 300,
                      text="Hi! \nEnjoy the game!",
                      justify=CENTER,
                      font="Verdana 40")
        # кнопка старт переміщає в інще вікно
        button_start = Button(
            self.root,
            text="START",
            width=35,
            height=7,
            font="Verdana 15",
            command=self.open_username_window)

        button_start.place(x=190, y=400)
        # автори тіпа
        c.create_text(530, 670,
                      text="by pythonlyanochka, shwei, lsdfr13",
                      justify=CENTER,
                      font="Verdana 20")

    def open_username_window(self):
        username_window = Toplevel(self.root)
        username_window.title("Enter Username")
        username_window.geometry("400x200")

        Label(username_window, text="Enter your name:",
              font="Verdana 15").pack(pady=20)
        self.username_entry = Entry(username_window,
                                    font="Verdana 15")
        self.username_entry.pack(pady=10)

        Button(username_window, text="Submit",
               command=lambda: self.submit_username(username_window),
               font="Verdana 15").pack(pady=20)

    def submit_username(self, username_window):
        username = self.username_entry.get()
        username_window.destroy()
        self.open_game_window(username)

    def open_game_window(self, username):
        game_window = Toplevel(self.root)
        game_window.title("SEA BATTLE")
        game_window.geometry("1500x1000")

        Label(game_window, text=f"Welcome, {username}!",
              font="Verdana 30").pack(pady=20)
        # Тут можна додати код для самої гри

if __name__ == "__main__":
    root = Tk()
    app = SeaBattleApp(root)
    root.mainloop()

