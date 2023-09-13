# SuperFastPython.com
# example of hosting a numpy array via a manager
from time import perf_counter
from multiprocessing.managers import BaseManager
from numpy import ones

# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass

# protect the entry point
if __name__ == '__main__':
    # register a function for creating numpy arrays
    CustomManager.register('shared_array', ones)
    # create and start the custom manager
    with CustomManager() as manager:
        # define the size of the numpy array
        n = 50000000
        # create a shared numpy array
        data_proxy = manager.shared_array((n,))
        print(f'Array created on host: {data_proxy}')
        # time sum operation on array in server process
        start = perf_counter()
        result = data_proxy.sum()
        duration = perf_counter() - start
        print(f'Sum hosted array {duration:.3f} sec')
        # time copy array and sum operation
        start = perf_counter()
        result = data_proxy._getvalue().sum()
        duration = perf_counter() - start
        print(f'Sum copied array {duration:.3f} sec')
