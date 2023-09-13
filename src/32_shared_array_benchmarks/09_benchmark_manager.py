# SuperFastPython.com
# benchmark of sharing a numpy array using manager
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from time import perf_counter
from numpy import ones

# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass

# task executed in a child process
def task(data_proxy):
    # report details of data
    print(f'>child has data: {data_proxy.sum()}')

# create a child process and share a numpy array
def main():
    # create and start the custom manager
    with CustomManager() as manager:
        # define the data
        n = 100000000
        # create a shared numpy array
        data_proxy = manager.shared_array((n,))
        # create a child process
        child = Process(target=task, args=(data_proxy,))
        # start the child process
        child.start()
        # wait for the child process to complete
        child.join()

# protect the entry point
if __name__ == '__main__':
    # register a function for creating numpy arrays
    CustomManager.register('shared_array', ones)
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
