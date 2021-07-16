"""
Define a function which can generate and print a tuple
where the value are square of numbers between 1 and 20 (both included).
"""


def gen_tup():
    return tuple(i ** 2 for i in range(20))


print(gen_tup())