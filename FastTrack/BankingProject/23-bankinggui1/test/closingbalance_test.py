from model.account import Account
from controller.account_parser import parse_account_file
from controller.transaction_parser import parse_transaction_file

if __name__ == "__main__":
    accounts_path = "../../data/accounts.json"
    transaction_path = "../../data/transactions.txt"

    parse_account_file(accounts_path)
    parse_transaction_file(transaction_path)

    for account_code, account in Account.get_accounts().items():
        print(account_code, account)
