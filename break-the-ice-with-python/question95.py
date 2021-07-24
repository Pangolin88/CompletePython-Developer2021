"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up.
"""

num = 5
scores = [2, 7, 3, 6, 6, 5]

unique_scores = set(scores)
sorted_scores = sorted(list(unique_scores))

print(sorted_scores[-2])
