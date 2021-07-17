"""
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.
"""


while True:
    email = input('Please input email: \n')
    if not email:
        break
    username = email.split('@')[0]
    print(f'Username: {username}')
