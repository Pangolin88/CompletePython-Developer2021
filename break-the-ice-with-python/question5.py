"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class MyString:
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


my_str = MyString()
my_str.get_string()
my_str.print_string()
