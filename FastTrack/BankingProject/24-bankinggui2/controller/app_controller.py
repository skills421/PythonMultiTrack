import json
from controller.account_parser import parse_account_file
from controller.transaction_parser import parse_transaction_file
from controller.custom_encoder import CustomEncoder
from model.account import Account
from view.banking_view import BankingView
import tkinter as tk
from pathlib import Path

class AppController:

    data_path = Path(__file__).parent.parent.joinpath('data')

    def __init__(self):
        window = tk.Tk()
        window.geometry("600x400+100+100")
        self.view = BankingView(window)
        self.init_button_handlers()
        self.accounts_file = None
        self.transaction_file = None

        window.mainloop()

    def init_button_handlers(self):
        self.view.accounts_btn.config(command=lambda: self.load_accounts())
        self.view.transactions_btn.config(command=lambda: self.load_transactions())
        self.view.process_btn.config(command=lambda: self.process_transactions())

    def get_file_content(self, filename):
        with open(filename, 'r') as f:
            content = f.read()

        return content

    def get_filename(self, title, description, definition):
        file_types = (description, definition),
        filename = self.view.get_file(AppController.data_path, title, file_types)
        return filename

    def load_accounts(self):
        self.accounts_file = self.get_filename('Load Accounts', 'account files', '*.json')
        content = self.get_file_content(self.accounts_file)
        self.view.write_account_details(content)
        self.view.select_accounts_tab()

    def load_transactions(self):
        self.transaction_file = self.get_filename('Load Transactions', 'transaction files', '*.txt')
        content = self.get_file_content(self.transaction_file)
        self.view.write_transaction_details(content)
        self.view.select_transaction_tab()

    def process_transactions(self):
        json_output = self.parse_data(self.accounts_file, self.transaction_file)
        self.view.write_output_details(json_output)
        self.view.select_output_tab()

    def parse_data(self, accounts_path, transaction_path):
        parse_account_file(accounts_path)
        parse_transaction_file(transaction_path)

        json_output = json.dumps(list(Account.get_accounts().values()), indent=4, cls=CustomEncoder)

        return json_output


