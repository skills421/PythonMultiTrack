import datetime


class Transaction:
    def __init__(self, transaction_date:datetime.datetime, transaction_type:str,
                 transaction_amount:float, third_party_account:int):
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.third_party_account = third_party_account

    def __str__(self):
        return str({
            "transaction_date": self.transaction_date,
            "transaction_type": self.transaction_type,
            "transaction_amount": self.transaction_amount,
            "third_party_account": self.third_party_account
        })

    def to_json(self):
        return {
            "transaction_date": self.transaction_date,
            "transaction_type": self.transaction_type,
            "transaction_amount": self.transaction_amount,
            "third_party_account": self.third_party_account
        }