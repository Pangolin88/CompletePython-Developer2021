"""
Input:
A given digit as the value of a.
Output:
Computes the value of a+aa+aaa+aaaa"""

from functools import reduce

num_as_char = input()

# using for loop
s = 0
for i in range(1, 5):
    s += int(num_as_char * i)
print(s)


# using reduce
def sum_num(s, i):
    return s + int(num_as_char * i)


print(reduce(sum_num, range(1, 5), 0))
