from model.account import Account
from model.transaction import Transaction
import datetime

account1 = Account(1234, opening_balance=350.00)
account2 = Account(2345, opening_balance=200.00)

Account.add_account(account1)
Account.add_account(account2)

for account_code, account in Account.get_accounts().items():
    print(account_code, account)

