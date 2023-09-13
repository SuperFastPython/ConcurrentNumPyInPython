# SuperFastPython.com
# benchmark of sharing a numpy array using pipe
from multiprocessing import Process
from multiprocessing import Pipe
from time import perf_counter
from numpy import ones

# task executed in a child process
def task(conn1):
    # receive the data
    data = conn1.recv()
    # report details of data
    print(f'>child has data: {data.shape}')

# create a child process and share a numpy array
def main():
    # create the shared queue
    conn1, conn2 = Pipe()
    # define the data
    n = 100000000
    data = ones((n,))
    # create a child process
    child = Process(target=task, args=(conn1,))
    # start the child process
    child.start()
    # share the data
    conn2.send(data)
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
