# SuperFastPython.com
# benchmark of sharing a numpy array ctype array
from multiprocessing import Process
from multiprocessing.sharedctypes import Array
from time import perf_counter
from numpy import ones
from numpy.ctypeslib import as_ctypes

# task executed in a child process
def task(array):
    # report details of data
    print(f'>child has data: {len(array)}')

# create a child process and share a numpy array
def main():
    # define the data
    n = 100000000
    data = ones((n,))
    # get ctype for our array
    ctype = as_ctypes(data)
    # create ctype array initialized from our array
    array = Array(ctype._type_, data, lock=False)
    # create a child process
    child = Process(target=task, args=(array,))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()

# protect the entry point
if __name__ == '__main__':
    # repeat the benchmark
    results = list()
    for i in range(3):
        # record start time
        time_start = perf_counter()
        # perform task
        main()
        # record duration
        time_duration = perf_counter() - time_start
        # report progress
        print(f'>{i} took {time_duration:.3f} seconds')
        # store result
        results.append(time_duration)
    # calculate average time
    time_avg = sum(results) / 3.0
    # report average time
    print(f'Average Time: {time_avg:.3f} seconds')
