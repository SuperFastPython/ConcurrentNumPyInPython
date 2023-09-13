# SuperFastPython.com
# example of sharing a numpy array via inheritance
from multiprocessing import set_start_method
from multiprocessing import Process
from numpy import ones
from numpy import zeros

# task executed in a child process
def task():
    # declare the global variable
    global data
    # check some data in the array
    print(data[:5,:5])
    # change data in the array
    data.fill(0.0)
    # confirm the data was changed
    print(data[:5,:5])

# protect the entry point
if __name__ == '__main__':
    # ensure we are using fork start method
    set_start_method('fork')
    # define the size of the numpy array
    n = 10000
    # create the numpy array
    data = ones((n,n))
    # create a child process
    child = Process(target=task)
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check some data in the array
    print(data[:5,:5])
