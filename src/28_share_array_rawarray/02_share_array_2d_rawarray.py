# SuperFastPython.com
# example of sharing 2d numpy array via ctype rawarray
from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray
from numpy import frombuffer
from numpy import double

# task executed in a child process
def task(array):
    # create a new numpy array backed by the raw array
    data = frombuffer(
        array, dtype=double, count=len(array))
    # reshape array into preferred shape
    data = data.reshape((3,3))
    # check the contents
    print(f'Child\n{data}')
    # increment the data
    data[:] += 1
    # confirm change
    print(f'Child\n{data}')

# protect the entry point
if __name__ == '__main__':
    # define the size of the numpy array
    n = 3*3
    # create the shared array
    array = RawArray('d', n)
    # create a new numpy array backed by the raw array
    data = frombuffer(
        array, dtype=double, count=len(array))
    # reshape array into preferred shape
    data = data.reshape((3,3))
    # populate the array
    data.fill(1.0)
    # confirm contents of the new array
    print(f'Parent\n{data}')
    # create a child process
    child = Process(target=task, args=(array,))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check some data in the shared array
    print(f'Parent\n{data}')
