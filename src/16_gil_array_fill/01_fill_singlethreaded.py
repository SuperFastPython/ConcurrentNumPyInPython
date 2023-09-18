# SuperFastPython.com
# example of single-threaded creating an array and fill
from time import perf_counter
from numpy import empty
# record the start time
start = perf_counter()
# create an empty array
n = 50000
data = empty((n,n))
# fill with 1s
data.fill(1)
# calculate the duration
duration = perf_counter() - start
# report the duration
print(f'Took {duration:.3f} seconds')
