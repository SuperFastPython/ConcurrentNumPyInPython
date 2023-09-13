# SuperFastPython.com
# benchmark of sharing a numpy array using inheritance
from multiprocessing import set_start_method
from multiprocessing import Process
from time import perf_counter
from numpy import ones

# task executed in a child process
def task():
    # declare the global variable
    global data
    # report details of data
    print(f'>child has data: {data.shape}')

# create a child process and share a numpy array
def main():
    # declare the global variable
    global data
    # define the global variable
    n = 100000000
    data = ones((n,))
    # create a child process
    child = Process(target=task)
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()

# protect the entry point
if __name__ == '__main__':
    # ensure we are using fork start method
    set_start_method('fork')
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
