"""
Define a custom exception class which takes a string message as attribute.
"""


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

raise MyCustomException('something went wrong!!!')
