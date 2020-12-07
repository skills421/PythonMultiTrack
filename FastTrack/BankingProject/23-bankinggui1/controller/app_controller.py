import json
from controller.account_parser import parse_account_file
from controller.transaction_parser import parse_transaction_file
from controller.custom_encoder import CustomEncoder
from model.account import Account
from view.banking_view import BankingView
import tkinter as tk
from pathlib import Path

class AppController:

    def __init__(self):
        window = tk.Tk()
        window.geometry("600x400+100+100")
        self.view = BankingView(window)
        window.mainloop()

    def parse_data(self, accounts_path, transaction_path):
        parse_account_file(accounts_path)
        parse_transaction_file(transaction_path)

        json_output = json.dumps(list(Account.get_accounts().values()), cls=CustomEncoder)

        return json_output


