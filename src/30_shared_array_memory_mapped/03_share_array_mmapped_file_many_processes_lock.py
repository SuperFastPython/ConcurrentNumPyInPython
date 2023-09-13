# SuperFastPython.com
# example of many processes changing mmapped with lock
from multiprocessing import Process
from multiprocessing import Lock
from numpy import memmap

# load shared array
def task(filename, shape, lock):
    # acquire lock
    with lock:
        # load the memory-mapped file
        data = memmap(filename,
            dtype='float32', mode='r+', shape=shape)
        # change the data
        data[:] += 1

# protect the entry point
if __name__ == '__main__':
    # define the size of the data
    shape = (100000000,)
    # define the filename
    filename = 'data.np'
    # create the memory-mapped file
    data = memmap(filename,
        dtype='float32', mode='w+', shape=shape)
    # populate the array
    data.fill(0.0)
    # check the status of the data
    print(data[:10])
    # create the shared lock
    lock = Lock()
    # create many child tasks
    children = [Process(target=task,
        args=(filename,shape,lock)) for _ in range(100)]
    # start all child tasks
    for child in children:
        child.start()
    # wait for all child tasks to complete
    for child in children:
        child.join()
    # check the status of the data
    print(data[:10])
