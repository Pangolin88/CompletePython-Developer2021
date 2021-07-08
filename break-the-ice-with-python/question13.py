"""
Input:
a sentence
Output:
Calculate the number of letters and digits.
"""
from functools import reduce

my_string = input()
# using for loop
count_digit, count_alpha = 0, 0
for i in my_string:
    if i.isdigit():
        count_digit += 1
    elif i.isalpha():
        count_alpha += 1

print(f'LETTERS: {count_alpha}')
print(f'DIGITS: {count_digit}')


# using reduce
def count_letters_digits(counters, char_to_check):
    counters[0] += char_to_check.isalpha()
    counters[1] += char_to_check.isnumeric()
    return counters


print('LETTERS {0}\nDIGITS {1}'.format(*reduce(count_letters_digits, my_string, [0, 0])))
