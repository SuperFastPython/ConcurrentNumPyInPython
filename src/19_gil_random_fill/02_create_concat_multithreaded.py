# SuperFastPython.com
# example creating arrays of random values in parallel
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from numpy import concatenate
from numpy import ceil
from numpy.random import SeedSequence
from numpy.random import default_rng

# create and return an array of random numbers
def create_array(seed, size):
    # create random number generator with the seed
    rand = default_rng(seed)
    # create array of random floats
    return rand.random(size=size)

# record start time
start = perf_counter()
# size of the array
n = 1000000000
# create a pool of workers
n_workers = 8
with ThreadPoolExecutor(n_workers) as exe:
    # create seeds for child processes
    seed_seq = SeedSequence(1)
    seeds = seed_seq.spawn(n_workers)
    # determine the size of each sub-array
    size = int(ceil(n / n_workers))
    # issue all tasks and gather results
    sizes = [size for _ in seeds]
    result_list = list(exe.map(create_array, seeds, sizes))
    # convert list of arrays into one large array
    result = concatenate(result_list)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
