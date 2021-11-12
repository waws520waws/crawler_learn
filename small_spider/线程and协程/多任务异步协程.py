import asyncio
import time
import scrapy
import requests  # requests模块是非异步模块

# 当遇到io等待，会自动执行在一个任务
async def request(url):
    print('正在下载：', url)
    # # 在异步协程中如果出现同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)
    # 应该这样写：
    # asyncio：实现异步
    # await：当遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完成')

start_time = time.time()


sema = asyncio.Semaphore(3)
# 为避免爬虫一次性请求次数太多，对并发量控制一下
async def x_get_source(url):
    with(await sema):
        await request(url)


urls = ['www.aaaa.com', 'www.bbbb.com', 'www.cccc.com', 'a', 'b', 'c']

# tasks = []
# for url in urls:
#     c = request(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
tasks = []
for url in urls:
    c = x_get_source(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)



# 生成或获取一个事件循环
loop = asyncio.get_event_loop()
# 需要将多任务列表封装到wait中，循环执行任务
loop.run_until_complete(asyncio.wait(tasks))

# # 上面两句等价于下面的执行语句（但是要注意括号里的对象）
# asyncio.run( asyncio.wait(tasks) )  # python3.7

print(time.time()-start_time)

