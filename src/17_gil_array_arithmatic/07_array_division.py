# SuperFastPython.com
# single-threaded matrix division with divide()
from time import perf_counter
from numpy import ones
from numpy import divide
from numpy import empty
# record start time
start = perf_counter()
# size of arrays
n = 50000
# create square matrices
data1 = ones((n, n))
data2 = ones((n, n))
result = empty((n, n))
# matrix division
_ = divide(data1, data2, out=result)
# calculate and report duration
duration = perf_counter() - start
print(f'Took {duration:.3f} seconds')
