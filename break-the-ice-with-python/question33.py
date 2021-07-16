"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
"""

def gen_lst():
    return [i ** 2 for i in range(20)]


print(gen_lst())