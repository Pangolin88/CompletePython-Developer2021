"""
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.
"""

import re


pattern = re.compile(r"\w@(\w+).\w")

while True:
    email = input('Please input email: \n')
    if not email:
        break
    company = pattern.search(email).group(1)
    print(f'Company: {company}')
