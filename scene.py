 from tkinter import *

class SeaBattleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SEA BATTLE")
        self.create_main_window()

    def create_main_window(self):
        c = Canvas(self.root, width=750, height=700)
        c.pack()

        # Прямокутник для "SEA BATTLE"
        margin_x = 0.05
        margin_y = 0.1
        c.create_rectangle(margin_x * 750, margin_y * 700, (1 - margin_x) * 750, 0.25 * 700)

        # Текст "SEA BATTLE"
        c.create_text(0.5 * 750, 0.15 * 700,
                      text="SEA BATTLE",
                      justify=CENTER,
                      font="Verdana 50")

        # Текст привітання
        c.create_text(0.5 * 750, 0.43 * 700,
                      text="Hi! \nEnjoy the game!",
                      justify=CENTER,
                      font="Verdana 40")

        # Кнопка "START"
        button_start = Button(
            self.root,
            text="START",
            width=20,
            height=2,
            font="Verdana 15",
            command=self.open_username_window)

        button_start.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Автори
        c.create_text(0.71 * 750, 0.96 * 700,
                      text="by pythonlyanochka, shwei, lsdfr13",
                      justify=CENTER,
                      font="Verdana 20")

    def open_username_window(self):
        username_window = Toplevel(self.root)
        username_window.title("Enter Username")
        username_window.geometry("400x200")

        Label(username_window, text="Enter your name:",
              font="Verdana 15").place(relx=0.5, rely=0.2, anchor=CENTER)
        self.username_entry = Entry(username_window,
                                    font="Verdana 15")
        self.username_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(username_window, text="Submit",
               command=lambda: self.submit_username(username_window),
               font="Verdana 15").place(relx=0.5, rely=0.8, anchor=CENTER)

    def submit_username(self, username_window):
        username = self.username_entry.get()
        username_window.destroy()
        self.open_game_window(username)

    def open_game_window(self, username):
        game_window = Toplevel(self.root)
        game_window.title("SEA BATTLE")
        game_window.geometry("1500x1000")

        Label(game_window, text=f"Welcome, {username}!",
              font="Verdana 30").place(relx=0.5, rely=0.1, anchor=CENTER)
        # Тут можна додати код для самої гри

if __name__ == "__main__":
    root = Tk()
    app = SeaBattleApp(root)
    root.mainloop()
