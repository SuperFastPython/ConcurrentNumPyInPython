# SuperFastPython.com
# example of returning an array from process via a queue
from multiprocessing import Process
from multiprocessing import Queue
from numpy import ones

# task executed in a child process
def task(queue):
    # define the size of the numpy array
    n = 1000
    # create the numpy array
    data = ones((n,n))
    # check some data in the array
    print(data[:5,:5])
    # send the array via a queue
    queue.put(data)

# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # create a child process
    child = Process(target=task, args=(queue,))
    # start the child process
    child.start()
    # read the data from the queue
    data = queue.get()
    # check some data in the array
    print(data[:5,:5])
