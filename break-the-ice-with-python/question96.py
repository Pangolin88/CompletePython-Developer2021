"""
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width.
"""


import textwrap

my_str = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4

print([print(sub_str) for sub_str in textwrap.wrap(my_str, w)])
