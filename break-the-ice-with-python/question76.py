"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""


import zlib

my_str = "hello world!hello world!hello world!hello world!"
my_str_encode = my_str.encode('utf-8')

my_str_compress = zlib.compress(my_str_encode)
print(my_str_compress)
print(zlib.decompress(my_str_compress))
