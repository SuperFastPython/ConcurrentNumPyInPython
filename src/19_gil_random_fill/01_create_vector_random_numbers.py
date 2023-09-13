# SuperFastPython.com
# create a large array of random numbers
from time import perf_counter
from numpy.random import rand
# record start time
start = perf_counter()
# size of the array
n = 1000000000
# create the array
array = rand(n)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
