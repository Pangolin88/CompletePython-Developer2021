from functools import reduce
my_string = input()

# using for loop
count_upper, count_lower = 0, 0
for i in my_string:
    if i.isupper():
        count_upper += 1
    if i.islower():
        count_lower += 1

print(f'UPPER CASE: : {count_upper}')
print(f'LOWER CASE: : {count_lower}')


# using reduce
def count_upper_lower(counters, char_to_check):
    counters[0] += char_to_check.isupper()
    counters[1] += char_to_check.islower()
    return counters


print('UPPER CASE: {0}\nLOWER CASE: {1}'.format(*(reduce(count_upper_lower, my_string, [0, 0]))))
