import re
date = input("enter email or mobile number :")
email_pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9.-]+.[a-zA-Z]$'
mobile_pattern = r'[0-9]{10}'
if re.fullmatch(email_pattern,date):
    print('valid')
elif re.fullmatch(mobile_pattern,date):
    print('valid number')
else:
    print('invalid')