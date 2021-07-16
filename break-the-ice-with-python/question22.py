"""
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
"""

from collections import Counter

# using collections.Counter
my_str = input().split(' ')
my_dict = dict(Counter(my_str))
for w in sorted(my_dict.keys()):
    print(f'{w}: {my_dict[w]}')


# using dict.count(key)
my_str = input().split(' ')
words = sorted(set(my_str))
for w in words:
    print(f'{w}: {my_str.count(w)}')
