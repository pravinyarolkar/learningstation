
# https://www.velotio.com/engineering-blog/asynchronous-programming-python-an-introduction

# Asynchronous programming has been gaining a lot of attention in the past few years, and for good reason. Although it can be more difficult than the traditional linear style, it is also much more efficient.

# For example, instead of waiting for an HTTP request to finish before continuing execution, with Python async coroutines you can submit the request and do other work that's waiting in a queue while waiting for the HTTP request to finish.

from multiprocessing import Process

def func_get_square(num, output):
    print("inside {}".format(func_get_square.__name__))
    output[num] = num

if __name__ == "__main__":
    procs = []
    import multiprocessing
    manager = multiprocessing.Manager()
    output = manager.dict()

    proc = Process(target=func_get_square, args=(1, output,))
    procs.append(proc)
    proc.start()

    inputs = [2,4,6,8,10]

    for num in inputs:
        proc = Process(target=func_get_square, args=(num,output,))
        procs.append(proc)
        proc.start()

    for prces in procs:
        prces.join()

    print(output)

    # same above code using queue
'''
from multiprocessing import Queue
    
def func_get_square(num, q):
    print("inside {}".format(func_get_square.__name__))
    q.put(num*num)

if __name__ == "__main__":
    procs = []
    queue = Queue()
    
    proc = Process(target=func_get_square, args=(1, queue,))
    procs.append(proc)
    proc.start()

    inputs = [2,4,6,8,10]

    for num in inputs:
        proc = Process(target=func_get_square, args=(num,queue,))
        procs.append(proc)
        proc.start()

    results = []

    for proc in procs:
        ret = queue.get()
        results.append(ret)

    for prces in procs:
        prces.join()

    print(results)
'''