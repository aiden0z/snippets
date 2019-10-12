# -*- coding:utf-8 -*-
# spider example for tornado

import time
from datetime import timedelta
try:
    from HTMLParser import HTMLParser
    from urlparse import urljoin, urldefrag
except ImportError:
    from html.parser import HTMLParser
    from urllib.parse import urljoin, urldefrag
from tornado import httpclient, gen, ioloop, queues

base_url = "http://www.tornadoweb.org/en/stable"
concurrency = 1


@gen.coroutine
def get_links_from_url(url):
    try:
        # 一定要使用异步http client
        response = yield httpclient.AsyncHTTPClient().fetch(url)
        # print("fetched %s" % url)
        html = response.body if isinstance(response.body, str) else response.body.decode()
        urls = [urljoin(url, remove_fragment(new_url)) for new_url in get_links(html)]
    except Exception as e:
        print("Exception: %s %s" % (e, url))
        raise gen.Return([])
    # 在 python 3.3 之前，不允许在 generator 中返回值，所以 tornado 采用 raise 一个异常的方式
    # 在 3.3 之后的版本可以使用 return urls
    raise gen.Return(urls)


def remove_fragment(url):
    pure_url, frag = urldefrag(url)
    return pure_url


def get_links(html):
    class URLSeeker(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.urls = []

        def handle_starttag(self, tag, attrs):
            href = dict(attrs).get("href")
            if href and tag == "a":
                self.urls.append(href)

    url_seeker = URLSeeker()
    url_seeker.feed(html)
    return url_seeker.urls


@gen.coroutine
def main():
    # 使用 tornado 实现的 queue
    q = queues.Queue()
    start = time.time()
    fetching, fetched = set(), set()

    @gen.coroutine
    def fetch_url():
        # 当 queue 中没有处理的url 时，该coroutine就会暂停执行
        current_url = yield q.get()
        try:
            if current_url in fetching:
                return
            # print("fetching %s" % current_url)
            fetching.add(current_url)
            urls = yield get_links_from_url(current_url)
            fetched.add(current_url)
            for new_url in urls:
                if new_url.startswith(base_url):
                    # 增加 queue 中 url 数量
                    yield q.put(new_url)
        finally:
            # 表示 queue 中的一个url已被处理，queue 中项减一个
            q.task_done()

    @gen.coroutine
    def worker():
        while True:
            yield fetch_url()

    q.put(base_url)
    for _ in range(concurrency):
        worker()

    # 等待所有coroutine 完成，超时时间为 300 s
    yield q.join(timeout=timedelta(seconds=300))
    assert fetching == fetched
    print("Done in %d seconds, fetched %s URLS." % (time.time() - start, len(fetched)))


if __name__ == "__main__":
    import logging
    logging.basicConfig()
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
