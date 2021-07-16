"""
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
"""


def max_len(str1, str2):
      if (len(str1) > len(str2)):
        print(str1)
      elif (len(str1) < len(str2)):
        print(str2)
      else:
        print(str1, str2)


max_len('Huynh', 'Ha')
max_len('Vi', 'Ha')
max_len('Ha', 'Huynh')