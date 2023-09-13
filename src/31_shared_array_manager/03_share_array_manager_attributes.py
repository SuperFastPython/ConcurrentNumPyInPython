# SuperFastPython.com
# example of accessing attribute of managed numpy array
from multiprocessing.managers import BaseManager
from numpy import ones

# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass

# helper wrapping a numpy array
class ArrayHelper():
    def __init__(self, dim):
        self.array = ones(dim)

    # access attributes on the numpy array
    def attribute(self, attr):
        return getattr(self.array, attr)

    # call functions on the numpy array
    def sum(self):
        return self.array.sum()

# protect the entry point
if __name__ == '__main__':
    # register the python class with the custom manager
    CustomManager.register('ArrayHelper', ArrayHelper)
    # create and start the custom manager
    with CustomManager() as manager:
        # define the size of the numpy array
        n = 100000000
        # create a shared numpy array
        data_proxy = manager.ArrayHelper((n,))
        print(f'Array created on host: {data_proxy}')
        # confirm content
        print(f'Array sum: {data_proxy.sum()}')
        # access shape of hosted array
        print(data_proxy.attribute('shape'))