# SuperFastPython.com
# multithreaded matrix square
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from numpy import ones
from numpy import square
from numpy import empty

# apply matrix math operation on a portion of a matrix
def task(coords, data, result):
    # unpack array indexes
    i1, i2, i3, i4 = coords
    _ = square(data[i1:i2,i3:i4],
        out=result[i1:i2,i3:i4])

# record start time
start = perf_counter()
# size of square arrays
n = 50000
# create square matrices
data = ones((n, n))
result = empty((n, n))
# create the thread pool
with ThreadPoolExecutor(4) as exe:
    # split each dimension (divisor of matrix dimension)
    split = round(n/2)
    # issue tasks
    for x in range(0, n, split):
        for y in range(0, n, split):
            # determine matrix coordinates
            coords = (x, x+split, y, y+split)
            # issue task
            _ = exe.submit(
                task, coords, data, result)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
