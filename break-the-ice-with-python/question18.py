"""
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
"""

import re

password = input().split(',')

for p in password:
    if re.match('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$#])([a-zA-Z0-9@$#]{6,12})$', p):
        print(p)
