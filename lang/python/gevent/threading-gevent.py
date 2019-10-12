# -*- coding:utf-8 -*-

import threading
from gevent import monkey, sleep
monkey.patch_all()


class ExcampleThread(threading.Thread):
    def run(self):
        for i in range(10):
            print "working"
        print "finish working"


class ExcampleThreadA(threading.Thread):
    def run(self):
        for i in range(10):
            print "working"
            sleep()
        print "finish working"

if __name__ == '__main__':
    # worker = ExcampleThread()
    worker = ExcampleThreadA()
    worker.start()
    print "this should be printed before the worker finished"
    worker.join()
