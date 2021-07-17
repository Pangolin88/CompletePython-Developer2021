"""
Define a class named American which has a static method called printNationality.
"""


class American:
    @staticmethod
    def printNationality():
        print("America")


person1 = American()

# This will not run if @staticmethod does not decorates the function. Because the class has no instance.
person1.printNationality()

# This will run even though the @staticmethod does not decorate printNationality()
American.printNationality()