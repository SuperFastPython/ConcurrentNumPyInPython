# SuperFastPython.com
# example of sharing a numpy array using a pipe
from multiprocessing import Process
from multiprocessing import Pipe
from numpy import ones

# task executed in a child process
def task(connection):
    # read the data from the pipe
    data = connection.recv()
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
    # create the shared pipe
    conn1, conn2 = Pipe()
    # create a child process
    child = Process(target=task, args=(conn1,))
    # start the child process
    child.start()
    # send the data to the child process
    conn2.send(data)
    # wait for the child process to complete
    child.join()
    # check some data in the array
    print(data[:5,:5])
