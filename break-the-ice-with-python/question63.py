"""
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
"""


def even_num(num):
    for i in range(num):
        if i % 2 == 0:
            yield i


num = int(input('Please input a number: \n'))
results = [str(i) for i in even_num(num + 1)]
print(', '.join(results))
