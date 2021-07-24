"""
With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all duplicate values with original order reserved.
"""


my_lst = [12,24,35,24,88,120,155,88,120,155]
result = []

for i in my_lst:
    if i not in result:
        result.append(i)

print(result)
