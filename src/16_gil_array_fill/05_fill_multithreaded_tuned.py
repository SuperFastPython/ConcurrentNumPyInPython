# SuperFastPython.com
# example of tuned multithreaded array fill
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from numpy import empty

# fill a portion of a larger array with a value
def fill_subarray(coords, data, value):
    # unpack array indexes
    i1, i2, i3, i4 = coords
    # populate subarray
    data[i1:i2,i3:i4].fill(value)

# record the start time
start = perf_counter()
# create an empty array
n = 50000
data = empty((n,n))
# create the thread pool
with ThreadPoolExecutor(8) as exe:
    # split each dimension
    split = round(n/4)
    # issue tasks
    for x in range(0, n, split):
        for y in range(0, n, split):
            # determine matrix coordinates
            coords = (x, x+split, y, y+split)
            # issue task
            _ = exe.submit(
                fill_subarray, coords, data, 1)
# calculate the duration
duration = perf_counter() - start
# report the duration
print(f'Took {duration:.3f} seconds')
