# SuperFastPython.com
# populate a large array with random numbers
from time import perf_counter
from numpy.random import default_rng
# from numpy.random import random
from numpy import empty
# record start time
start = perf_counter()
# size of the array
n = 1000000000
# create the array
array = empty(n)
# create random number generator with the seed
rand = default_rng(seed=1)
# populate the array
rand.random(out=array)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
