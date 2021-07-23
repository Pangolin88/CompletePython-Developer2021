"""
By using list comprehension, please write a program to print the list
after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""

my_lst = [12,24,35,70,88,120,155]


# using comprehensive
print([value for index, value in enumerate(my_lst) if index % 2])
