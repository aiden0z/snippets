# -*- coding:utf-8 -*-

import Queue
import socket
from functools import partial
from tornado.ioloop import IOLoop

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

server_addr = ("localhost", 10000)
sock.bind(server_addr)
sock.listen(5)

fd_map = {}
message_queue_map = {}
fd = sock.fileno()
fd_map[fd] = sock

ioloop = IOLoop.instance()


def handle_client(cli_addr, fd, event):
    s = fd_map[fd]
    if event & IOLoop.READ:
        data = s.recv(1024).strip()
        if data:
            print("recevied {0} from {1}".format(data, cli_addr))
            # update fd stat
            ioloop.update_handler(fd, IOLoop.WRITE)
            message_queue_map[s].put(data)
        else:
            print("closing {0}".format(cli_addr))
            ioloop.remove_handler(fd)
            s.close()
            del message_queue_map[s]
    if event & IOLoop.WRITE:
        try:
            next_msg = message_queue_map[s].get_nowait()
        except Queue.Empty:
            print("{0} queue empty".format(cli_addr))
            ioloop.update_handler(fd, IOLoop.READ)
        else:
            print("sending {0} to {0}".format(next_msg, cli_addr))
            s.send(next_msg + "\n")
    if event & IOLoop.ERROR:
        print("Exception on {0}".format(cli_addr))
        ioloop.remove_handler(fd)
        s.close()
        del message_queue_map[s]


def handle_server(fd, event):
    s = fd_map[fd]
    if event & IOLoop.READ:
        conn, cli_addr = s.accept()
        print("Connection {0}".format(cli_addr[0]))
        conn.setblocking(0)
        conn_fd = conn.fileno()
        fd_map[conn_fd] = conn
        handle = partial(handle_client, cli_addr[0])
        # register handler and connection
        ioloop.add_handler(conn_fd, handle, IOLoop.READ)
        message_queue_map[conn] = Queue.Queue()


ioloop.add_handler(fd, handle_server, IOLoop.READ)
ioloop.start()
