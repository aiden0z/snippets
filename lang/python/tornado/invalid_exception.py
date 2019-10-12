# -*- coding:utf-8 -*-

# out() 函数中捕捉不到异常.
# 但是在实践当中, 因为 callback 的调用, 间接地是由 func 造成的,
# 通常我们希望的一个结果是, callback 抛出的异常,
# 应该就像是 func 抛出的异常一样, 触发对应的异常处理, 输出 ok
# 注意, 这里对异常的行为, 我们只说 像 func 抛出的,
# 或者说, 一个非 func 抛出的异常, 与一个就是由 func 抛出的异常, 它们会造成相同的结果, 这是本质的问题.

import tornado.ioloop

IL = tornado.ioloop.IOLoop.instance()


def callback():
    raise Exception("in callback")


def func():
    IL.add_callback(callback)


def out():
    try:
        func()
    except:
        print("ok")


# out()
# IL.start()
# 为了达到" callback 抛出的异常, 就像是 func 抛出的一样 " , 这个目的, 我们最直观地会想到这样处理代码:


def callback1():
    try:
        raise Exception("in callback")
    except:
        print("ok")

# 或者这样的代码


def like_other(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("ok")
    return wrapper

# IL.add_callbak(like_other(callback))

# 现在让我们实现正确的方式


def func1():
    IL.add_callback(lambda: env(callback))


def env(func):
    try:
        func()
    except:
        print("ok")


def out1():
    env(func1)

#  env(func1)
#  IL.start()

# 以上代码当然没有问题， 这样做当然没有问题, 除了代码逻辑上的一个缺陷
# -- func1 需要知道它的调用者, out1 中的细节, 即 func1 要知道 out1 在调用它
# 时挖了一个叫 env 的坑. 这个问题就大了, 而且很显然地, 调用 func1 的地方可能有许多,
# 除了 env 它们还使用着各种不同的坑. 所以在 func1 中写死了 env 这点必须得到改进.
# 比如引入一个中间的容器

HOLE= {}


def func2():
    IL.add_callback(lambda: HOLE[""](callback))


def env1(func):
    try:
        func()
    except:
        print("ok")


def out2():
    HOLE.setdefault("", env1)
    env1(func2)

out2()
IL.start()

# 至此, 理想状态下问题似乎得到解决了. 但是实践当中, 情况则会复杂得多, 有不同的 out ,
# 不同的 env , 但是基本的处理方式是没有变的, 我们把 env 抽象成函数执行的"上下文",
# 把 HOLE 抽象成一个全局的上下文管理容器, 两者配合, 就可以实现出更通用的结构.
