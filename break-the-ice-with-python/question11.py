"""
Input:
Write a program which accepts a sequence of comma separated 4 digit binary numbers
Output:
check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
"""

lst_bi_num = input().split(',')
lst_result = []

# using for loop
for num in lst_bi_num:
    if int(num, 2) % 5 == 0:
        lst_result.append(num)
print(','.join(lst_result))

# using short-hand
lst_result = [num for num in lst_bi_num if int(num, 2) % 5 == 0]
print(','.join(lst_result))


# using filter
def check(x):
    return int(x, 2) % 5 == 0


lst_result = list(filter(check, lst_bi_num))
print(','.join(lst_result))
