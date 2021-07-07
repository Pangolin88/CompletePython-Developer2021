"""
Input:
Write a program that accepts sequence of lines
Output:
Prints the lines after making all characters in the sentence capitalized.
"""

# using while loop
result = []
while True:
    s = input()
    if not s:
        break
    else:
        result.append(s.upper())

for item in result:
    print(item)


# using generator
def input_str():
    while True:
        s = input()
        if not s:
            return
        else:
            yield s.upper()


print(*(s for s in input_str()), sep='\n')
