# SuperFastPython.com
# example of multithreaded matrix least squares solution
from os import environ
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import lstsq
# record the start time
start = perf_counter()
# size of arrays
n = 5000
# create matrix
a = rand(n, n)
# create result
b = rand(n, 1)
# solve least squares equation
x, _, _, _ = lstsq(a, b, rcond=None)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
