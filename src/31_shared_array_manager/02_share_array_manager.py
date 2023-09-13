# SuperFastPython.com
# example of sharing a numpy array using a manager
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from numpy import ones

# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass

# task executed in a child process
def task(data_proxy):
    # report details of the array
    print(f'Array sum (in child): {data_proxy.sum()}')

# protect the entry point
if __name__ == '__main__':
    # register a function for creating numpy arrays
    CustomManager.register('shared_array', ones)
    # create and start the custom manager
    with CustomManager() as manager:
        # define the size of the numpy array
        n = 100000000
        # create a shared numpy array
        data_proxy = manager.shared_array((n,))
        print(f'Array created on host: {data_proxy}')
        # confirm content
        print(f'Array sum: {data_proxy.sum()}')
        # start a child process
        process = Process(
            target=task, args=(data_proxy,))
        process.start()
        process.join()