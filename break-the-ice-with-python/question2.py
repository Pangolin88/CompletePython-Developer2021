"""
Input:
Write a program which can compute the factorial of a given numbers.
Output:
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""
from functools import reduce

num = int(input('Please input a number: '))


# using for loop
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


print(factorial(num))


# using short-hand
def short_fact(x): return 1 if x <= 1 else x * short_fact(x - 1)


# using reduce
def fun(acc, item):
    print(f'{acc} - {item} - {acc * item}')
    return acc * item


print(reduce(fun, range(1, num + 1), 1))


"""
reduce output when num = 8
1 - 1 - 1
1 - 2 - 2
2 - 3 - 6
6 - 4 - 24
24 - 5 - 120
120 - 6 - 720
720 - 7 - 5040
5040 - 8 - 40320
40320
"""
