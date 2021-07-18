"""
Please write a program using generator to print the numbers
which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console
"""


def my_func(num):
    for i in range(num):
        if i % 35 == 0:
            yield i


num = int(input('Please input a number: \n'))
results = [str(i) for i in my_func(num + 1)]
print(', '.join(results))
