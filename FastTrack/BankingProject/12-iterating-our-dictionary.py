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

    return {'record_type':record_type, 'file_date':file_date, 'client_records':client_records}

#
# - Client Header
#

def parse_client_header(record):
    record_type = record[0:2]
    account_no_hex = record[2:6]
    account_no_dec = int(account_no_hex, 16)
    transaction_records = int(record[6:])

    return {
        'record_type':record_type,
        'account_no_dec':account_no_dec,
        'transaction_records':transaction_records
    }

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

    return {
        'record_type':record_type,
        'transaction_date':transaction_date,
        'transaction_type':transaction_type,
        'transaction_amount':transaction_amount,
        'third_party_account':third_party_account
    }

#
# - File Footer
#

def parse_file_footer(record):
    record_type = record[0:2]

    return {'record_type':record_type}

#
# -- Parse the incoming record
#

def parse_record(record):
    detail = ()
    record_type = record[0:2]

    if record_type == 'FH':
        detail = parse_file_header(record)

    elif record_type == 'CH':
        detail = parse_client_header(record)

    elif record_type == 'CT':
        detail = parse_client_transaction(record)

    elif record_type == 'FF':
        detail = parse_file_footer(record)

    return detail

#
# -- print the detail record
#

def print_detail(detail):
    for field in detail:
        value = detail[field]
        print(field, value)
#
    print()
# - Invoke all the record parsers
#

records = [
    'FH19032019:23020002',
    'CH1ABC0002',
    'CT19032019:080414D000000000023.5500001431759372813465',
    'CT19032019:132508D000000000147.1400001948847238383813',
    'FF'
]

for record in records:
    detail = parse_record(record)
    print_detail(detail)
