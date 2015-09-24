# -*- coding:utf-8 -*-

import time
import gevent
from gevent import select


start = time.time()
tic = lambda: "at %1.1f seconds" % (time.time() - start)


def gr1():
    print("Started Polling 1 :%s" % tic())
    select.select([], [], [], 2)
    print("Ended Polling 1: %s" % tic())


def gr2():
    print("Started Polling 2:%s" % tic())
    select.select([], [], [], 2)
    print("Ended Polling 2: %s" % tic())


def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)
    print("Get here")


def gr4():
    print("I get the order")


gevent.joinall([gevent.spawn(gr1), gevent.spawn(gr2), gevent.spawn(gr3), gevent.spawn(gr4)])
