"""
Define a class named American and its subclass NewYorker.
"""


class American:
    pass


class NewYorker(American):
    pass


american = American()
newyorker = NewYorker()

print(american)
print(newyorker)

print(isinstance(american, American))
print(isinstance(newyorker, NewYorker))
print(isinstance(american, NewYorker))
print(isinstance(newyorker, American))
