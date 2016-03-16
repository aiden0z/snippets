# -*- coding:utf-8 -*-
# spider example for tornado

from tornado import gen, ioloop, httpclient

base_url = "http://www.tornadoweb.org/en/stable"


@gen.coroutine
def f():
    # 一定要使用异步http client
    response = yield httpclient.AsyncHTTPClient().fetch(base_url)
    # print("fetched %s" % url)
    print response.headers

if __name__ == "__main__":
    io_loop = ioloop.IOLoop.current().run_sync(f)
