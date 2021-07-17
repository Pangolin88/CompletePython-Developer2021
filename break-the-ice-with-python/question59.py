"""
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
"""

from functools import reduce


num = int(input())
s = 0


# using for loop
for i in range(1, num + 1):
    s +=  i/(i + 1)

print(round(s, 2))


# using map
print(round(sum(map(lambda i: i/(i + 1), range(1, num + 1))), 2))


# using reduce
print(round(reduce(lambda s, i: s + i/(i + 1), range(1, num + 1), 0), 2))
