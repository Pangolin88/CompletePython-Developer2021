"""
Please write a program to print the running time of execution of "1+1" for 100 times.
"""

import time


start_time = time.time()
for i in range(100):
    1 + 1

end_time = time.time()
print(f'Running time of execution: {end_time - start_time}')
