"""
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""


class Person:
    pass


class Male(Person):
    def getGender(self):
        print('male')


class Female(Person):
    def getGender(self):
        print('female')


zelda = Female()
zelda.getGender()
