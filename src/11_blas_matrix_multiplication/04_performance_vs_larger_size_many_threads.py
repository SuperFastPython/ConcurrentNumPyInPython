# SuperFastPython.com
# benchmark of multithreaded matrix multiplication
from os import environ
environ['OMP_NUM_THREADS'] = '4'
from time import perf_counter
from numpy.random import rand

# multiply two matrices and report how long it takes
def task(n, repeats=30):
    results = list()
    for _ in range(repeats):
        # record start time
        start = perf_counter()
        # create an array of random values
        data1 = rand(n, n)
        data2 = rand(n, n)
        # matrix multiplication
        result = data1.dot(data2)
        # calculate the duration in seconds
        duration = perf_counter() - start
        # store result
        results.append(duration)
    # return the average
    return sum(results) / repeats

# report time of matrix multiplication for each size
for size in range(2000,11000,2000):
    # perform task and record time
    result = task(size)
    # report result
    print(f'{size} took {result:.6f} seconds')
