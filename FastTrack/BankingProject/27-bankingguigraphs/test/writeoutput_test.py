from controller.custom_encoder import CustomEncoder
from model.account import Account
from controller.account_parser import parse_account_file
from controller.transaction_parser import parse_transaction_file
import json

if __name__ == "__main__":
    accounts_path = "../../data/accounts.json"
    transaction_path = "../../data/transactions.txt"

    parse_account_file(accounts_path)
    parse_transaction_file(transaction_path)

    for account_code, account in Account.get_accounts().items():
        print(account_code, account)

    json_output = json.dumps(list(Account.get_accounts().values()), cls=CustomEncoder)

    print(json_output)
