# SuperFastPython.com
# example of matrix multiplication (tuned numpy threads)
from os import environ
# set threads equal to number of physical cores
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy.random import rand

# function for creating a test matrix
def load_data(n=2000):
    # square matrix of random floats
    return rand(n, n)

# function for performing operation on matrices
def operation(item1, item2):
    # matrix multiplication
    return item1.dot(item2)

# record the start time
start = perf_counter()
# load data
data1 = [load_data() for _ in range(100)]
data2 = [load_data() for _ in range(100)]
# apply operation to items
results = [operation(item1, item2)
    for item1,item2 in zip(data1,data2)]
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
