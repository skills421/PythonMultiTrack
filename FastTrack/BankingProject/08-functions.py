import datetime

#
# -- File Header
#


def parse_file_header(record):
    record_type = record[0:2]
    file_date_str = record[2:15]

    file_date = datetime.datetime(
        int(file_date_str[4:8]),  # year
        int(file_date_str[2:4]),  # month
        int(file_date_str[0:2]),  # day
        int(file_date_str[9:11]),  # hour
        int(file_date_str[11:13])  # minute
    )

    client_records = int(record[15:])

    print(record)

    print(record_type)
    print(file_date_str)
    print(file_date)
    print(client_records)
    print()

#
# - Client Header
#

def parse_client_header(record):
    record_type = record[0:2]
    account_no_hex = record[2:6]
    account_no_dec = int(account_no_hex, 16)
    transaction_records = int(record[6:])

    print(record)
    print(record_type)
    print(account_no_hex)
    print(account_no_dec)
    print(transaction_records)
    print()

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

    print(record)
    print(record_type)
    print(transaction_date_str)
    print(transaction_date)
    print(transaction_type)
    print(transaction_amount)
    print(third_party_account)
    print()

#
# - File Footer
#

def parse_file_footer(record):
    record_type = record[0:2]

    print(record)
    print(record_type)
    print()

#
# - Invoke all the record parsers
#

parse_file_header('FH19032019:23020002')
parse_client_header('CH1ABC0002')
parse_client_transaction('CT19032019:080414D000000000023.5500001431759372813465')
parse_client_transaction('CT19032019:132508D000000000147.1400001948847238383813')
parse_file_footer('FF')
