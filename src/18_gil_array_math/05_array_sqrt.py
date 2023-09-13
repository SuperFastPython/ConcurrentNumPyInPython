# SuperFastPython.com
# single-threaded matrix sqrt
from time import perf_counter
from numpy import ones
from numpy import sqrt
# record start time
start = perf_counter()
# size of arrays
n = 50000
# create square matrix
data = ones((n, n))
# matrix sqrt
result = sqrt(data)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
