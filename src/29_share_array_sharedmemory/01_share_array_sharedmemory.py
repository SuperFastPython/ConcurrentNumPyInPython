# SuperFastPython.com
# example of sharing a numpy array via a sharedmemory
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
from numpy import ones
from numpy import ndarray
import numpy

# task executed in a child process
def task():
    # define the size of the numpy array
    n = 10000
    # attach another shared memory block
    sm = SharedMemory('MyMemory')
    # create a new numpy array that uses shared memory
    data = ndarray(
        (n,), dtype=numpy.double, buffer=sm.buf)
    # check the contents
    print(f'Child {data[:10]}')
    # increment the data
    data[:] += 1
    # confirm change
    print(f'Child {data[:10]}')
    # close the shared memory
    sm.close()

# protect the entry point
if __name__ == '__main__':
    # define the size of the numpy array
    n = 10000
    # bytes required for the array (8 bytes per value)
    n_bytes = n * 8
    # create the shared memory
    sm = SharedMemory(
        name='MyMemory', create=True, size=n_bytes)
    # create a new numpy array that uses shared memory
    data = ndarray(
        (n,), dtype=numpy.double, buffer=sm.buf)
    # populate the array
    data.fill(1.0)
    # confirm contents of the new array
    print(data[:10], len(data))
    # create a child process
    child = Process(target=task)
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check some data in the shared array
    print(data[:10])
    # close the shared memory
    sm.close()
    # release the shared memory
    sm.unlink()
