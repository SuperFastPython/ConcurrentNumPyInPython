# SuperFastPython.com
# simpler example of sharing array via a sharedmemory
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
from multiprocessing.managers import SharedMemoryManager
from numpy import ones
from numpy import ndarray
import numpy

# define a numpy array backed by shared memory
def sm_array(shared_mem, shape, dtype=numpy.double):
    # create a new numpy array that uses shared memory
    return ndarray(
        shape, dtype=dtype, buffer=shared_mem.buf)

# task executed in a child process
def task(n, name):
    # attach another shared memory block
    sm = SharedMemory(name)
    # create a new numpy array that uses shared memory
    data = sm_array(sm, (n,))
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
    n = 10000000
    # bytes required for the array (8 bytes per value)
    n_bytes = n * 8
    with SharedMemoryManager() as smm:
        # create the shared memory
        sm = smm.SharedMemory(size=n_bytes)
        # create a new array that uses shared memory
        data = sm_array(sm, (n,))
        # populate the array
        data.fill(1.0)
        # confirm contents of the new array
        print(data[:10], len(data))
        # create a child process
        child = Process(target=task, args=(n, sm.name))
        # start the child process
        child.start()
        # wait for the child process to complete
        child.join()
        # check some data in the shared array
        print(data[:10])
