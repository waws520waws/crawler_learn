
import asyncio
import time
import aiohttp
import aiofiles

start_time = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]

async def get_page(url):
    # requests 属于同步模块,所以这里不用
    # async：声明后面跟的是异步操作
    async with aiohttp.ClientSession(headers={}, cookies='') as session:
        async with session.get(url, params={}, headers={}) as response:
            if response == 200:
                # 注意：获取响应数据之前一定要进行手动挂起
                page = await response.text()

                # 文件异步
                async with aiofiles.open() as f:
                    await f.write(page)

tasks = []
for url in urls:
    xc = get_page(url)
    task = asyncio.ensure_future(xc)
    tasks.append(task)

# 生成或获取一个事件循环
loop = asyncio.get_event_loop()
# 循环执行任务
loop.run_until_complete(asyncio.wait(tasks))

# # 上面两句等价于下面的执行语句（但是要注意括号里的对象）
# asyncio.run( asyncio.wait(tasks) )  # python3.7

print(time.time()-start_time)


