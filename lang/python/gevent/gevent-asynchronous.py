# -*- coding:utf-8 -*-

import gevent
import random
import time




def task(pid):
    """
    some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2) * 0.001)
    print("Task %s done" % pid)


def synchronous():
    start = time.time()
    for i in range(1, 10):
        task(i)
    print("Total time :%f" % (time.time() - start))


def asynchronous():
    start = time.time()
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)
    print("Total time :%f" % (time.time() - start))


print("Synchronous:")
synchronous()


print("Asynchronous:")
asynchronous()
