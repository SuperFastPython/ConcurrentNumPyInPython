# SuperFastPython.com
# example of sharing a shared ctype array
from multiprocessing import Process
from multiprocessing.sharedctypes import Array
from numpy import ones
from numpy.ctypeslib import as_ctypes

# task executed in a child process
def task(array):
    # check some data in the array
    print(array[:10], len(array))
    # change data in the array
    for i in range(len(array)):
        array[i] = 0.0
    # confirm the data was changed
    print(array[:10], len(array))

# protect the entry point
if __name__ == '__main__':
    # define the size of the numpy array
    n = 10000
    # create the numpy array
    data = ones((n,))
    print(data[:10], data.shape)
    # get ctype for our array
    ctype = as_ctypes(data)
    # create ctype array initialized from our array
    array = Array(ctype._type_, data, lock=False)
    # confirm contents of the shared array
    print(array[:10], len(array))
    # create a child process
    child = Process(target=task, args=(array,))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check some data in the shared array
    print(array[:10], len(array))
