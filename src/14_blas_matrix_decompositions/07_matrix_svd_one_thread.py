# SuperFastPython.com
# single-threaded svd matrix decomposition
from os import environ
environ['OMP_NUM_THREADS'] = '1'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import svd
# record start time
start = perf_counter()
# size of matrix to create
n = 3000
# create a square matrix of random floats
matrix = rand(n, n)
# perform decomposition
u, s, vh = svd(matrix)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
