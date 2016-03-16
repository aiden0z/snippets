#!/usr/bin/env python
# encoding: utf-8

from contextlib import contextmanager, nested


@contextmanager
def make_context():
    print "enter"
    try:
        yield {}
    except RuntimeError, err:
        print "error", err
    finally:
        print "exit"

with make_context() as value:
    print "inside with statement:", value


@contextmanager
def make_context(name):
    print 'entering', name
    yield name
    print 'exiting', name

# 同时管理三个上下文
with nested(make_context('A'), make_context('B'), make_context('C')) as (A, B, C):
    print 'inside with statement:', A, B, C


@contextmanager
def process():
    try:
        yield 123
    except Exception as e:
        print type(e)

# 异常被捕捉
with process() as i:
    print type(i)
    raise Exception(2)
