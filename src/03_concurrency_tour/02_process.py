# SuperFastPython.com
# example of running a function in a new process
from time import sleep
from multiprocessing import Process

# task that blocks for a moment and prints a message
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('This is coming from another process',
        flush=True)

# entry point for the program
if __name__ == '__main__':
    # define a task to run in a new process
    process = Process(target=task)
    # start the task in a new process
    process.start()
    # display a message
    print('Waiting for the new process to finish...')
    # wait for the task to complete
    process.join()
