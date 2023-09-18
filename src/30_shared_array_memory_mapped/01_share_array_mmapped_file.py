# SuperFastPython.com
# example of sharing a memory-mapped numpy array
from multiprocessing import Process
from numpy import memmap

# load shared array
def task(filename, n):
    # load the memory-mapped file
    data = memmap(filename,
        dtype='float32', mode='r+', shape=(n,))
    # check the status of the data
    print(f'Child: {data[:10]}')
    # change the data
    data[:] += 1
    # flush the changes
    data.flush()
    # check the status of the data
    print(f'Child: {data[:10]}')

# protect the entry point
if __name__ == '__main__':
    # define the size of the data
    n = 1000
    # define the filename
    filename = 'data.np'
    # create the memory-mapped file
    data = memmap(filename,
        dtype='float32', mode='w+', shape=(n,))
    # populate the array
    data.fill(1.0)
    # flush the changes
    data.flush()
    # check the status of the data
    print(data[:10])
    # create a child process
    child = Process(target=task, args=(filename,n))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check the status of the data
    print(data[:10])
