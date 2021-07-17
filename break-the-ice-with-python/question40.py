"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""


input_str = input()

if input_str in ('YES', 'yes', 'Yes'):
    print('Yes')
else:
    print('No')