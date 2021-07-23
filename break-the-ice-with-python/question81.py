"""
By using list comprehension, please write a program to print the list
after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""


my_lst = [12,24,35,70,88,120,155]


# using filter
print(list(filter(lambda i: i % 35, my_lst)))


# using comprehensive
print([i for i in my_lst if i % 35])
