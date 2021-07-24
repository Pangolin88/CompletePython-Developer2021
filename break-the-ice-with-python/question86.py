"""
By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].
"""


my_lst = [12,24,35,24,88,120,155]
print([i for i in my_lst if i != 24])
