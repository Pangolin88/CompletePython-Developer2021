"""
Input:
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Output:
Write a program that computes the net amount of a bank account based a transaction log from console input.
"""

total_amount = 0
while True:
    s = input()
    if not s:
        break
    else:
        action, amount = s.split(' ')
        if action == 'D':
            total_amount += int(amount)
        elif action == 'W':
            total_amount -= int(amount)

print(total_amount)
