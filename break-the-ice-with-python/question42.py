"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""


my_lst = range(1, 11)

square_even_lst = list(map(lambda i: i ** 2, list(filter(lambda i: i % 2 == 0, my_lst))))
print(square_even_lst)
