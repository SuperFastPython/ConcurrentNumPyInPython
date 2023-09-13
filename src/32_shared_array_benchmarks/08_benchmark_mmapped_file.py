# SuperFastPython.com
# benchmark of sharing a numpy array using mmapped file
from multiprocessing import Process
from time import perf_counter
from numpy import memmap

# task executed in a child process
def task(filename, n):
    # load the memory mapped file
    data = memmap(filename,
        dtype='float32', mode='r+', shape=(n,))
    # report details of data
    print(f'>child has data: {data.shape}')

# create a child process and share a numpy array
def main():
    # define the size of the data
    n = 100000000
    # define the filename
    filename = 'data.np'
    # create the memory mapped file
    data = memmap(filename,
        dtype='float32', mode='w+', shape=(n,))
    # populate the array
    data.fill(1.0)
    # create a child process
    child = Process(target=task, args=(filename, n))
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
