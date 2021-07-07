"""
Input:
Write a program that accepts a comma separated sequence of words
Output:
Prints the words in a comma-separated sequence after sorting them alphabetically.
"""

seq = input().split(',')
seq.sort()
print(','.join(seq))