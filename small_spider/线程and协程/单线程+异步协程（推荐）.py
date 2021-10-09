# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/


'''
单线程+异步协程实现异步IO操作.
- 什么是异步IO
    - 所谓「异步 IO」，就是你发起一个 IO阻塞 操作，却不用等它结束，你可以继续做其他事情，当它结束时，你会得到通知。

- event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。

- coroutine：中文翻译叫协程，在 Python 中常指代为协程对象类型，我们可以将协程对象注册到事件循环中，它会被事件循环调用。
我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。

- task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

- future：代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。只是调用方式不同

- async/await 关键字，它是从 Python 3.5 才出现的，专门用于定义协程。其中，async 定义一个协程，await 用来挂起阻塞方法的执行。

'''

## 在python3.4之后新增了asyncio模块，可以帮我们检测IO阻塞，然后实现异步IO。
## 注意：asyncio只能发tcp级别的请求，不能发http协议。

import asyncio

async def request(url):
    print('正在请求url：', url)
    print('请求成功')
    return '回调函数的返回值^^'

# async修饰的函数，调用之后返回的是一个协程对象(函数里的语句不会立马执行)
xc = request('www.qq1234.com')

## 1、

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到loop中， 然后启动loop（函数在此处启动执行）
# loop.run_until_complete(xc)

## 2、task、future的使用

# loop = asyncio.get_event_loop()
# # 创建一个task对象
# task = loop.create_task(xc)
# # # future的使用同理，只是调用方式不同
# # task = asyncio.ensure_future(xc)
# print(task)  # 查看此时任务的状态（未执行）
# # 任务执行
# loop.run_until_complete(task)
# print(task)  # 查看此时任务的状态（已完成）

## 3、绑定回调

def callback_func(task):
    # result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())

task = asyncio.ensure_future(xc)
# 将回调函数绑定到任务对象中（参数为任务对象task）
task.add_done_callback(callback_func)

# 生成或获取一个事件循环
loop = asyncio.get_event_loop()
# 循环执行任务
loop.run_until_complete(task)

# # 上面两句等价于下面的执行语句（但是要注意括号里的对象）
# asyncio.run(task)  # python3.7
