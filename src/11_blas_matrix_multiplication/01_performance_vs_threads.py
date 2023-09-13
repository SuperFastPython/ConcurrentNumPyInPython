# SuperFastPython.com
# benchmark matrix multiplication
from os import environ
environ['OMP_NUM_THREADS'] = '1'
from time import perf_counter
from numpy.random import rand

# multiply two matrices and return how long it takes
def task(n):
    # record start time
    start = perf_counter()
    # create an array of random values
    data1 = rand(n, n)
    data2 = rand(n, n)
    # matrix multiplication
    result = data1.dot(data2)
    # calculate the duration in seconds
    duration = perf_counter() - start
    # return the result
    return duration

# repeat the experimental task and return average result
def experiment(n, repeats=10):
    # repeat the experiment and gather results
    results = [task(n) for _ in range(repeats)]
    # return the average of the results
    return sum(results) / repeats

# size of the matrix to test
n = 5000
# perform task and record time
result = experiment(n)
# report result
print(f'{n} took {result:.6f} seconds')
