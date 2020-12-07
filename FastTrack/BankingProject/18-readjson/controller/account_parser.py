import json
from model.account import Account

#
# - globals
#

accounts = []


#
# - methods
#

def parse_account_file_content(content):
    global accounts
    parsed_content = json.loads(content)

    for parsed_account in parsed_content.get('accounts'):
        account_code = parsed_account.get('id')
        opening_balance = parsed_account.get('balance')

        account = Account(account_code, opening_balance=opening_balance)
        accounts.append(account)



def parse_account_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        parse_account_file_content(content)


#
# -- Test
#

file_path = "../../data/accounts.json"
parse_account_file(file_path)

for account in accounts:
    print(account)
