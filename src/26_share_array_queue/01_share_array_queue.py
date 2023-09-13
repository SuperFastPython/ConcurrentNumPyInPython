# SuperFastPython.com
# example of sharing a numpy array using a queue
from multiprocessing import Process
from multiprocessing import Queue
from numpy import ones

# task executed in a child process
def task(queue):
    # read data from the shared queue (blocking)
    data = queue.get()
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
    # create the shared queue
    queue = Queue()
    # create a child process
    child = Process(target=task, args=(queue,))
    # start the child process
    child.start()
    # send the data to the child process
    queue.put(data)
    # wait for the child process to complete
    child.join()
    # check some data in the array
    print(data[:5,:5])
