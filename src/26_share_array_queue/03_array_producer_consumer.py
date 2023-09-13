# SuperFastPython.com
# example of array producers and consumers with a queue
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import JoinableQueue
from numpy import ones

# producer task that adds arrays to the queue
def producer_task(queue):
    # create a fixed number of arrays
    for _ in range(5):
        # create a numpy array
        n = 2000
        data = ones((n,n))
        # push into the queue
        queue.put(data)
        # report message
        print('Producer added array.', flush=True)
        # sleep some amount of time
        sleep(random())

# consumer task that reads arrays from the queue
def consumer_task(queue):
    # read arrays
    while True:
        # read one array
        data = queue.get()
        # check for final item
        if data is None:
            # report message
            print('Consumer done.', flush=True)
            # exit the task
            break
        # report a message
        print(f'Consumer read an array {data.shape}',
            flush=True)
        # mark the item as done
        queue.task_done()

# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = JoinableQueue()
    # start producer tasks
    producers = [Process(target=producer_task,
        args=(queue,)) for _ in range(4)]
    for process in producers:
        process.start()
    # start consumer task
    consumer = Process(target=consumer_task,
        args=(queue,))
    consumer.start()
    # wait for all producers to be done
    for process in producers:
        process.join()
    # wait until all items have been marked done
    queue.join()
    # signal that there are no more tasks
    queue.put(None)
    # wait for the consumer process to be done
    consumer.join()
    # report a final message
    print('Done.', flush=True)
