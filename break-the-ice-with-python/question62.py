"""
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Input: 7
Output: 0,1,1,2,3,5,8,13
"""


num = int(input('Please input a number: \n'))


def fibo(num):
    if num == 0 or num == 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


results = [fibo(i) for i in range(num + 1)]
print(results)
