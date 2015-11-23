#!/usr/bin/env python
# encoding: utf-8

import tornado.ioloop
import tornado.web
import os

settings = {
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "src/static")}

template_path = os.path.join(os.path.dirname(__file__), "src")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        files = os.listdir('src')
        files.remove('index.html')
        self.render('index.html', files=files)


class MainHandler(tornado.web.RequestHandler):
    def get(self, file):
        self.render(file)

handlers = [
    (r"/", IndexHandler),
    (r"/(.*)", MainHandler)]

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=handlers,
        template_path=template_path,
        **settings)
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
