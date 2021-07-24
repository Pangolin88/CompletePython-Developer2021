"""
Please write a program which count and print the numbers of each character in a string input by console.
"""


from collections import Counter

my_str = input()
result = dict(Counter(my_str))

[print(f'{char}:{count}') for char, count in result.items()]
