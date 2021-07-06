"""
Input:
With a given integral number n
Output:
write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
"""

# using for loop
num = int(input('Please input a number: '))
dct = {}
for i in range(1, num + 1):
    dct[i] = i ** 2

print(dct)

# using dictionary comprehension
print({i: i * i for i in range(1, num + 1)})

# using enumerate
print(dict(enumerate([i * i for i in range(1, num + 1)], 1)))

