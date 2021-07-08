"""
Input:
Numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
Output:
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

lst_result = []

# using for loop
for i in range(1000, 3001):
    if i % 2 == 0:
        lst_result.append(str(i))
print(','.join(lst_result))

# using short-hand
lst_result = [str(i) for i in range(1000, 3001) if i % 2 == 0]
print(','.join(lst_result))


# using filter and map
def check(x):
    return x % 2 == 0


lst_result = map(str, list(filter(check, range(1000, 3001))))
print(','.join(lst_result))

# using lambda instead of function check
lst_result = map(str, list(filter(lambda x: x % 2 == 0, range(1000, 3001))))
print(','.join(lst_result))
