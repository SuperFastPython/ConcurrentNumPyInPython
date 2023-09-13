# SuperFastPython.com
# example of returning an array from a child process
from multiprocessing import Process
from multiprocessing import Pipe
from numpy import ones

# task executed in a child process
def task(pipe):
    # define the size of the numpy array
    n = 10000
    # create the numpy array
    data = ones((n,n))
    # check some data in the array
    print(data[:5,:5])
    # send the array via a pipe
    pipe.send(data)

# protect the entry point
if __name__ == '__main__':
    # create the shared pipe
    conn1, conn2 = Pipe()
    # create a child process
    child = Process(target=task, args=(conn2,))
    # start the child process
    child.start()
    # read the data from the pipe
    data = conn1.recv()
    # check some data in the array
    print(data[:5,:5])
