"""
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
"""


my_lst = [5,6,77,45,22,12,24]


# using filter
print(list(filter(lambda i: i % 2, my_lst)))


# using comprehensive
print([i for i in my_lst if i % 2])
