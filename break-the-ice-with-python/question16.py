"""
Input:
The list is input by a sequence of comma-separated numbers.
Output:
Use a list comprehension to square each odd number in a list.
"""

lst_num = map(int, input().split(','))

result = [str(i*i) for i in lst_num if i % 2 == 1]
print(','.join(result))
