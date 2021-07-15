"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""


class MyGen:
    def __init__(self, num):
        self.num = num + 1

    def is_divisible_by_7(self):
        for i in range(self.num):
            if i % 7 == 0:
                yield i

    def print_result(self):
        [print(i) for i in self.is_divisible_by_7()]


gen = MyGen(30)
gen.print_result()
