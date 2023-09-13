# SuperFastPython.com
# example of multithreaded matrix power
from os import environ
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import matrix_power
# record the start time
start = perf_counter()
# size of arrays
n = 4000
# create an array of random values
data = rand(n, n)
# matrix power
result = matrix_power(data, 10)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
