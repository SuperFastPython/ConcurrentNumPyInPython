# SuperFastPython.com
# example of multithreaded matrix determinant
from os import environ
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy import ones
from numpy.linalg import det
# record the start time
start = perf_counter()
# size of arrays
n = 10000
# create a data array
data = ones((n, n))
# matrix determinant
result = det(data)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
