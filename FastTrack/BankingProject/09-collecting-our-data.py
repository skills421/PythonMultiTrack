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

    return record_type, file_date, client_records

#
# - Client Header
#

def parse_client_header(record):
    record_type = record[0:2]
    account_no_hex = record[2:6]
    account_no_dec = int(account_no_hex, 16)
    transaction_records = int(record[6:])

    return record_type, account_no_dec, transaction_records

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

    return record_type, transaction_date, transaction_type, transaction_amount, third_party_account

#
# - File Footer
#

def parse_file_footer(record):
    record_type = record[0:2]

    return record_type,

#
# -- print the detail record
#

def print_detail(detail):
    print(detail)

#
# - Invoke all the record parsers
#

detail = parse_file_header('FH19032019:23020002')
print_detail(detail)


detail = parse_client_header('CH1ABC0002')
print_detail(detail)

detail = parse_client_transaction('CT19032019:080414D000000000023.5500001431759372813465')
print_detail(detail)

detail = parse_client_transaction('CT19032019:132508D000000000147.1400001948847238383813')
print_detail(detail)

detail = parse_file_footer('FF')
print_detail(detail)
