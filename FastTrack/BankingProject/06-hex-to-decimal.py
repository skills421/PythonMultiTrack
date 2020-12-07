file_header_record = 'FH19032019:23020002'
#                     0123456789012345678

#
# -- File Header
#

record_type = file_header_record[0:2]
file_date = file_header_record[2:15]
client_records = int(file_header_record[15:])

print(file_header_record)

print(record_type)
print(file_date)
print(client_records)
print()

#
# - Client Header
#

client_header_record = 'CH1ABC0002'
record_type = client_header_record[0:2]
account_no_hex = client_header_record[2:6]
account_no_dec = int(account_no_hex, 16)
transaction_records = int(client_header_record[6:])

print(client_header_record)
print(record_type)
print(account_no_hex)
print(account_no_dec)
print(transaction_records)
print()

#
# - Client Transaction
#

client_transaction_record = 'CT19032019:080414D000000000023.5500001431759372813465'
record_type = client_transaction_record[0:2]
transaction_date = client_transaction_record[2:17]
transaction_type = client_transaction_record[17]
transaction_amount = float(client_transaction_record[18:37])
third_party_account = int(client_transaction_record[37:])

print(client_transaction_record)
print(record_type)
print(transaction_date)
print(transaction_type)
print(transaction_amount)
print(third_party_account)
print()

#
# - File Footer
#

file_footer_record = 'FF'
record_type = file_footer_record[0:2]

print(file_footer_record)
print(record_type)
print()