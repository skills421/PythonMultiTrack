import sys
import tkinter as tk
from tkinter import ttk


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

        self.init_left_bar_buttons()
        self.init_right_bar_buttons()
        self.init_input_frame()
        self.init_output_frame()
        self.init_bottom_frame()

    def init_menu(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='Close', command=lambda: sys.exit())

    def init_left_bar_buttons(self):
        frame = tk.Frame(self.window, bd=5)
        frame.place(relx=0.25, rely=0.02, relheight=0.1, anchor='n')

        self.accounts_btn = ttk.Button(frame, text='Upload Accounts')
        self.accounts_btn.pack(side=tk.LEFT, fill=tk.X)

        self.transactions_btn = ttk.Button(frame, text='Upload Transactions')
        self.transactions_btn.pack(side=tk.LEFT, fill=tk.X)

    def init_right_bar_buttons(self):
        frame = tk.Frame(self.window, bd=5)
        frame.place(relx=0.75, rely=0.02, relheight=0.1, anchor='n')

        self.process_btn = ttk.Button(frame, text='Process Transactions')
        self.process_btn.pack(side=tk.LEFT, fill=tk.X)

        self.analyse_btn = ttk.Button(frame, text='Analyse Transactions')
        self.analyse_btn.pack(side=tk.LEFT, fill=tk.X)

    def init_input_frame(self):
        frame = tk.Frame(self.window, bd=5)
        frame.place(relx=0.25, rely=0.14, relheight=0.72, relwidth=0.46, anchor='n')

        self.input_tab_control = ttk.Notebook(frame)
        self.input_tab_control.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.accounts_tab = tk.Frame(self.input_tab_control)
        self.transactions_tab = tk.Frame(self.input_tab_control)

        self.input_tab_control.add(self.accounts_tab, text='Accounts File')
        self.input_tab_control.add(self.transactions_tab, text='Transactions File')

    def init_output_frame(self):
        frame = tk.Frame(self.window, bd=5)
        frame.place(relx=0.75, rely=0.14, relheight=0.72, relwidth=0.46, anchor='n')

        self.output_tab_control = ttk.Notebook(frame)
        self.output_tab_control.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.output_tab = tk.Frame(self.output_tab_control)
        self.output_tab_control.add(self.output_tab, text='Output File')

    def init_bottom_frame(self):
        frame = tk.Frame(self.window, bd=5, bg='blue')
        frame.place(relx=0.5, rely=0.88, relheight=0.1, relwidth=0.96, anchor='n')