from controller.app_controller import parse_data

accounts_path = "../data/accounts.json"
transaction_path = "../data/transactions.txt"

if __name__ == "__main__":
    json_output = parse_data(accounts_path, transaction_path)
    print(json_output)
