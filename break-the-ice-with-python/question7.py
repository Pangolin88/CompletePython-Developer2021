"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
"""

x, y = map(int, input().split(","))

result = []
for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i * j)
    result.append(tmp)

print(result)

result = [[i * j for j in range(y)] for i in range(x)]

print(result)
