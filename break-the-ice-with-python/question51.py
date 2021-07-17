"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""


def divide(num):
    try:
        return num/0
    except ZeroDivisionError as err:
        raise err
    except:
        raise 'something went wrong!!!'


divide(5)
