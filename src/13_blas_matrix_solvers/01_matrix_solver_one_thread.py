# SuperFastPython.com
# example of single-threaded matrix solver
from os import environ
environ['OMP_NUM_THREADS'] = '1'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import solve
# record the start time
start = perf_counter()
# size of arrays
n = 8000
# create matrix
a = rand(n, n)
# create result
b = rand(n, 1)
# solve least squares equation
x = solve(a, b)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
