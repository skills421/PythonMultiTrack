import datetime

#
# - Transaction Class
#


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


#
# - Account Class
#

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


#
# - Client Header
#

def parse_client_header(record):
    record_type = record[0:2]
    account_no_hex = record[2:6]
    account_no_dec = int(account_no_hex, 16)
    transaction_records = int(record[6:])

    account = Account(account_no_dec, transaction_records)

    return account

#
# - Client Transaction
#

def parse_client_transaction(record):
    record_type = record[0:2]
    transaction_date_str = record[2:17]

    transaction_date = datetime.datetime(
        int(transaction_date_str[4:8]),     # year
        int(transaction_date_str[2:4]),     # month
        int(transaction_date_str[0:2]),     # day
        int(transaction_date_str[9:11]),    # hour
        int(transaction_date_str[11:13]),   # minute
        int(transaction_date_str[13:15])    # seconds
    )

    transaction_type = record[17]
    transaction_amount = float(record[18:37])
    third_party_account = int(record[37:])

    transaction = Transaction(transaction_date, transaction_type, transaction_amount, third_party_account)

    return transaction


#
# - Test
#

account1 = parse_client_header('CH1ABC0002')

transaction1 = parse_client_transaction('CT19032019:080414D000000000023.5500001431759372813465')
account1.add_transaction(transaction1)

transaction2 = parse_client_transaction('CT19032019:132508D000000000147.1400001948847238383813')
account1.add_transaction(transaction2)

print(account1)


