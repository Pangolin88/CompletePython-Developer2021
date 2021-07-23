"""
By using list comprehension, please write a program to print the list
after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
"""

my_lst = [12,24,35,70,88,120,155]


# using comprehensive
print([i for i in my_lst if i not in my_lst[2:5]])

