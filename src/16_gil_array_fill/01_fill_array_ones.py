# SuperFastPython.com
# example of single-threaded filling an array
from time import perf_counter
from numpy import ones
# record the start time
start = perf_counter()
# create a new matrix and fill with 1
n = 50000
data = ones((n,n))
# calculate the duration
duration = perf_counter() - start
# report the duration
print(f'Took {duration:.3f} seconds')
