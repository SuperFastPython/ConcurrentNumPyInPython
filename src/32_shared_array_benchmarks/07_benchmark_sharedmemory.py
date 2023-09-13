# SuperFastPython.com
# benchmark of sharing a numpy array with sharedmemory
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
from time import perf_counter
from numpy import ndarray
from numpy import double

# task executed in a child process
def task(n):
    # attach another shared memory block
    sm = SharedMemory('MyMemory')
    # create a new numpy array that uses shared memory
    data = ndarray((n,), dtype=double, buffer=sm.buf)
    # report details of data
    print(f'>child has data: {data.shape}')
    # close the shared memory
    sm.close()

# create a child process and share a numpy array
def main():
    # define the size of the array
    n = 100000000
    # bytes required for the array (8 bytes per value)
    n_bytes = n * 8
    # create the shared memory
    sm = SharedMemory(
        name='MyMemory', create=True, size=n_bytes)
    # create a new numpy array that uses shared memory
    data = ndarray((n,), dtype=double, buffer=sm.buf)
    # populate the array
    data.fill(1.0)
    # create a child process
    child = Process(target=task, args=(n,))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # release the shared memory
    sm.unlink()

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
