# SuperFastPython.com
# example of single-threaded matrix pseudo inverse
from os import environ
environ['OMP_NUM_THREADS'] = '1'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import pinv
# record the start time
start = perf_counter()
# size of array
n = 3000
# create an array of random values
data = rand(n, n)
# matrix pseudo inverse
result = pinv(data)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
