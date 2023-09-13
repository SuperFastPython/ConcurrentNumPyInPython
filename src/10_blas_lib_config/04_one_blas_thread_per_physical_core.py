# SuperFastPython.com
# example with one blas thread per physical core
from os import environ
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy.random import rand
# record the start time
start = perf_counter()
# size of arrays
n = 8000
# create an array of random values
data1 = rand(n, n)
data2 = rand(n, n)
# matrix multiplication
result = data1.dot(data2)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
