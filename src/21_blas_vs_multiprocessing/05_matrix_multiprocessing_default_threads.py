# SuperFastPython.com
# example with multiprocessing (default blas threads)
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
from numpy.random import rand

# function for creating a test matrix
def load_data(n=2000):
    # square matrix of random floats
    return rand(n, n)

# function for performing operation on matrices
def operation(item1, item2):
    # matrix multiplication
    return item1.dot(item2)

# function that defines a single task
def task(value):
    # load items
    item1 = load_data()
    item2 = load_data()
    # perform operation
    result = operation(item1, item2)

# entry point
if __name__ == '__main__':
    # record the start time
    start = perf_counter()
    # create process pool
    with ProcessPoolExecutor(4) as exe:
        # issue tasks
        _ = exe.map(task, range(100))
    # calculate and report duration
    duration = perf_counter() - start
    print(f'Took {duration:.3f} seconds')
