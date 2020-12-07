import datetime
from model.transaction import Transaction


class Account:
    def __init__(self, account_code:int, transaction_count:int):
        self.account_code = account_code
        self.transaction_count = transaction_count
        self.transactions = []

    def __str__(self):
        return str({
            "account_code": self.account_code,
            "transaction_count": self.transaction_count,
            "transactions": [eval(str(_transaction)) for _transaction in self.transactions]
        })

    def add_transaction(self, transaction:Transaction):
        self.transactions.append(transaction)