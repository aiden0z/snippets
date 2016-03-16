#!/usr/bin/env python
# encoding: utf-8

"""
Tornado 中两种异步 handler 的实现方式
"""

import tornado


class CoroutineHandler(tornado.web.RequestHanlder):
    """
    使用 gen.coroutine 实现的异步handler
    """
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://friendfeed-api.com/v2/feed/bret")
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries from API")


class AsyncHandler(tornado.web.RequestHandler):
    """
    使用 tornado.web.asyncronous 装饰器时，直到调用 self.finish 才会返回 response
    也就是说浏览器发出请求，tornado 执行 self.get() 后，整个 request 流程还未完成
    浏览器一直会hang住（转圈）直到 self.finish() 被执行, 才真正返回 response。
    """
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://friendfeed-api.com/v2/feed/bret",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries "
                   "from the FriendFeed API")
        self.finish()
