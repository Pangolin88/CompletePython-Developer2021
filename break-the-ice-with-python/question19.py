"""
You are required to write a program to sort the (name, age, score) tuples
by ascending order where name is string, age and score are numbers.
The priority is that name > age > score.
The tuples are input by console.
"""

from operator import itemgetter

data = []
while True:
    input_data = input()
    if not input_data:
        break
    tuple_data = tuple(input_data.split(','))
    data.append(tuple_data)


# using lambda
data.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(data)

# using itemgetter
print(sorted(data, key=itemgetter(0, 1, 2)))
