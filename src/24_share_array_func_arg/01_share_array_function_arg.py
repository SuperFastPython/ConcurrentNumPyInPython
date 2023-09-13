# SuperFastPython.com
# example of sharing a numpy array via function argument
from multiprocessing import Process
from numpy import ones

# task executed in a child process
def task(data):
    # check some data in the array
    print(data[:5,:5])
    # change data in the array
    data.fill(0.0)
    # confirm the data was changed
    print(data[:5,:5])

# protect the entry point
if __name__ == '__main__':
    # define the size of the numpy array
    n = 10000
    # create the numpy array
    data = ones((n,n))
    # create a child process
    child = Process(target=task, args=(data,))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check some data in the array
    print(data[:5,:5])
