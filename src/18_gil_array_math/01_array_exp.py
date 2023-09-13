# SuperFastPython.com
# single-threaded matrix exp
from time import perf_counter
from numpy import ones
from numpy import exp
# record start time
start = perf_counter()
# size of arrays
n = 50000
# create square matrix
data = ones((n, n))
# matrix exp
result = exp(data)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
