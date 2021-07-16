"""
Define a function which can generate a list
where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.
"""

def gen_lst():
    return [i ** 2 for i in range(20)][-5:]


print(gen_lst())
