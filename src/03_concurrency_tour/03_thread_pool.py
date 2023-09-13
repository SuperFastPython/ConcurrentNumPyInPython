# SuperFastPython.com
# demonstration with the thread pool life-cycle
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# task that blocks for a moment and prints a message
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('Task running in a worker thread')
    # return a message
    return 'All done'

# create the pool of worker threads
with ThreadPoolExecutor() as exe:
    # execute a task in another thread
    future = exe.submit(task)
    # display a message
    print('Waiting for the task to finish...')
    # wait for the task to finish and get the result
    result = future.result()
    # report the result
    print(result)
