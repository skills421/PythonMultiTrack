file_header_record = 'FH19032019:23020002'

print('FH19032019:23020002')
print(file_header_record)

record_type = 'FH'
file_date = '19032019:2302'
client_records = '0002'

print(record_type)
print(file_date)
print(client_records)

client_header_record = 'CH1ABC0002'
record_type = 'CH'
account_no = '1ABC'
transaction_records = '0002'

print(client_header_record)
print(record_type)
print(account_no)
print(transaction_records)

client_transaction_record = 'CT19032019:080414D000000000023.5500001431759372813465'
record_type = 'CT'
transaction_date = '19032019:080414'
transaction_type = 'D'
transaction_amount = '000000000023.550000'
third_party_account = '1431759372813465'

print(client_transaction_record)
print(record_type)
print(transaction_date)
print(transaction_type)
print(transaction_amount)
print(third_party_account)

file_footer_record = 'FF'
record_type = 'FF'

print(file_footer_record)
print(record_type)