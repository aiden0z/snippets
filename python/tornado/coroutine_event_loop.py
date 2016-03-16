# -*- coding:utf-8 -*-

from bisect import insort
from collections import deque
from functools import partial
from time import time
import selectors
import sys
import types


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n


class sleep_for_seconds(object):
    def __init__(self, wait_time):
        self._wait_time = wait_time


class EventLoop(object):
    def __init__(self, *tasks):
        self._running = False
        self._selector = selectors.DefaultSelector()
        self._tasks = deque(tasks)
        self._tasks_waiting_on_stdin = []
        self._timers = []
        self._selector.register(sys.stdin, selectors.EVENT_READ)

    def resume_task(self, coroutine, value=None, stack=()):
        print("h1")
        result = coroutine.send(value)
        print("h2")
        if isinstance(result, types.GeneratorType):
            self.schedule(result, None, (coroutine, stack))
        elif isinstance(result, sleep_for_seconds):
            self.schedule(coroutine, None, stack, time() + result._wait_time)
        elif result is sys.stdin:
            self._tasks_waiting_on_stdin.append((coroutine, stack))
        elif stack:
            self.schedule(stack[0], result, stack[1])

    def schedule(self, coroutine, value=None, stack=(), when=None):
        task = partial(self.resume_task, coroutine, value, stack)
        if when:
            insort(self._timers, (when, task))
        else:
            self._tasks.append(task)

    def stop(self):
        self._running = False

    def do_on_next_tick(self, func, *args, **kwargs):
        self._tasks.appendleft(partial(func, *args, **kwargs))

    def run_forever(self):
        self._running = True
        while self._running:
            for key, mask in self._selector.select(0):
                line = key.fileobj.readline().strip()
                for task, stack in self._tasks_waiting_on_stdin:
                    self.schedule(task, line, stack)
                self._tasks_waiting_on_stdin.clear()

            if self._tasks:
                task = self._tasks.popleft()
                print(task)
                task()

            while self._timers and self._timers[0][0] < time():
                task = self._timers[0][1]
                del self._timers[0]
                task()
        self._running = False


def print_every(message, interval):
    while True:
        print("{} - {}".format(int(time()), message))
        yield sleep_for_seconds(interval)


def read_input(loop):
    while True:
        line = yield sys.stdin
        if line == "exit":
            loop.do_on_next_tick(loop.stop)
            continue
        n = int(line)
        print("fib({}) = {}".format(n, fib(n)))


def main():
    loop = EventLoop()
    hello_task = print_every("hello world!", 3)
    fib_task = read_input(loop)
    loop.schedule(hello_task)
    loop.schedule(fib_task)
    loop.run_forever()

if __name__ == "__main__":
    main()
