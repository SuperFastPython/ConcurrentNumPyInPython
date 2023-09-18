# SuperFastPython.com
# example populating a large array in parallel
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from numpy import ceil
from numpy import empty
from numpy.random import SeedSequence
from numpy.random import default_rng

# populate a subsequence of a large array
def populate(seed, array, ix_start, ix_end):
    # create random number generator with the seed
    rand = default_rng(seed)
    # populate a subsequence of the large array
    rand.random(out=array[ix_start:ix_end])

# record start time
start = perf_counter()
# size of the array
n = 1000000000
# create array
array = empty(n)
# create the pool of workers
n_workers = 8
with ThreadPoolExecutor(n_workers) as exe:
    # create seeds for child processes
    seed_seq = SeedSequence(1)
    seeds = seed_seq.spawn(n_workers)
    # determine the size of each subsequence
    size = int(ceil(n / n_workers))
    # issue all tasks
    _ = [exe.submit(populate, seeds[i], array,
        i*size, (i+1)*size) for i in range(n_workers)]
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
