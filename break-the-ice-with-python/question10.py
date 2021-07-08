"""
Input:
Write a program that accepts a sequence of whitespace separated words as input.
Output:
Prints the words after removing all duplicate words and sorting them alphanumerically.
"""

my_lst = input().split(' ')
my_lst = list(set(my_lst))
my_lst.sort()

print(' '.join(my_lst))
