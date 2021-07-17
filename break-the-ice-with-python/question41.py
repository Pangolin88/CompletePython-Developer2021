"""
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""


my_lst = range(1, 11)


def square(i):
  return i ** 2


# using function
square_lst = list(map(square, my_lst))
print(square_lst)


# using lambda
square_lst = list(map(lambda i: i ** 2, my_lst))
print(square_lst)