"""
Please write a program to generate all sentences
where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""


import itertools

subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]

sentence = [subject, verb, object]

print(list(itertools.product(*sentence)))
