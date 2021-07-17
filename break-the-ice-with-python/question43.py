"""
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""


my_lst = range(1, 21)

even_lst = list(filter(lambda i: i % 2 == 0, my_lst))
print(even_lst)
