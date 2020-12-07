import sys
import tkinter as tk


class BankingView(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.init_window()

    def init_window(self):
        self.window.title('Banking Transaction')

        self.window.lift()
        self.window.attributes('-topmost', True)

        self.init_menu()

    def init_menu(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='Close', command=lambda: sys.exit())