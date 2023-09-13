# SuperFastPython.com
# example of single-threaded matrix inverse
from os import environ
environ['OMP_NUM_THREADS'] = '1'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import inv
# record the start time
start = perf_counter()
# size of arrays
n = 5000
# create an array of random values
data = rand(n, n)
# matrix inverse
result = inv(data)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
