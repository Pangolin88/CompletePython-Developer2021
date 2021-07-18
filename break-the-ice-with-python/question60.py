"""
f(n)=f(n-1)+100 when n>0
and f(0)=0
"""


num = int(input('Please input a number: \n'))

def my_func(num):
    if num == 0:
        return 0
    return my_func(num - 1) + 100


print(my_func(num))
