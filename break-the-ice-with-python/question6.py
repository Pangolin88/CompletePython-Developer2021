"""
Input:
Write a program that calculates and prints the value according to the given formula:
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Output:
Q = Square root of [(2 * C * D)/H]
"""
import math

c = 50
h = 30
seq = input().split(",")
my_lst = [str(int(math.sqrt((2 * c * int(d)) / h))) for d in seq]
print(','.join(my_lst))
