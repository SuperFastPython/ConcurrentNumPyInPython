# SuperFastPython.com
# demonstration with the process pool life-cycle
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# task that blocks for a moment and prints a message
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('Task running in a worker process',
        flush=True)
    # return a message
    return 'All done'

# demonstrate the process pool
def main():
    # create the pool of worker processes
    with ProcessPoolExecutor() as exe:
        # execute a task in another process
        future = exe.submit(task)
        # display a message
        print('Waiting for the task to finish...')
        # wait for the task to finish and get the result
        result = future.result()
        # report the result
        print(result)

# entry point
if __name__ == '__main__':
    main()
