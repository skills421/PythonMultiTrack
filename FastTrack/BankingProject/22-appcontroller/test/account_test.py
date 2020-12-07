from model.account import Account
from model.transaction import Transaction
import datetime

account_code = 1234
opening_balance = 350.00

transaction_date_str = '19032019:080414'

transaction_date = datetime.datetime(
    int(transaction_date_str[4:8]),     # year
    int(transaction_date_str[2:4]),     # month
    int(transaction_date_str[0:2]),     # day
    int(transaction_date_str[9:11]),    # hour
    int(transaction_date_str[11:13]),   # minute
    int(transaction_date_str[13:15])    # seconds
)

transaction_type = 'C'
transaction_amount = 25.15
third_party_account = 1234567890

account1 = Account(account_code, opening_balance=opening_balance)
print(account1)

transaction1 = Transaction(transaction_date, transaction_type, transaction_amount, third_party_account)
print(transaction1)

account1.add_transaction(transaction1)
print(account1)

