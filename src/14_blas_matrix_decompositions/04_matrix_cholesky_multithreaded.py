# SuperFastPython.com
# multithreaded cholesky matrix decomposition
from os import environ
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy.random import rand
from numpy.linalg import cholesky
# record start time
start = perf_counter()
# size of matrix to create
n = 8000
# create a square matrix of random floats
matrix = rand(n, n)
# ensure it is positive definite
matrix = matrix.dot(matrix.T)
# perform decomposition
l = cholesky(matrix)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
