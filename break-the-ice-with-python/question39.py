"""
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""


my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_tup = tuple(i for i in my_tup if i % 2 == 0)
print(even_tup)