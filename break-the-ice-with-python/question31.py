"""
Define a function which can print a dictionary
where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
"""

def gen_dct():
    return {i: i ** 2 for i in range(20)}


print(gen_dct())
