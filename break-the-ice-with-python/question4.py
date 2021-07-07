"""
Input:
Write a program which accepts a sequence of comma-separated numbers from console
Output:
generate a list and a tuple which contains every number.Suppose the following input is supplied to the program
"""

seq = input('Please in out a sequence of comma-separated numbers\n')
print(seq.split(","))
print(tuple(seq.split(",")))
