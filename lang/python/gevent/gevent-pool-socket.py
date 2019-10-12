# -*- coding:utf-8 -*-

from gevent.pool import Pool


class SocketPool(object):

    def __init__(self):
        self.pool = Pool(100)
        self.pool.start()

    def listen(self, socket):
        while True:
            socket.recv()
