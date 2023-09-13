# SuperFastPython.com
# benchmark of sharing a numpy array ctype rawarray
from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray
from time import perf_counter
from numpy import frombuffer
from numpy import double

# task executed in a child process
def task(data):
    # report details of data
    print(f'>child has data: {data.shape}')

# create a child process and share a numpy array
def main():
    # create the raw array
    n = 100000000
    array = RawArray('d', n)
    # create numpy array from raw array buffer
    data = frombuffer(array, dtype=double,
        count=len(array))
    # populate the array
    data.fill(1.0)
    # create a child process
    child = Process(target=task, args=(data,))
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
