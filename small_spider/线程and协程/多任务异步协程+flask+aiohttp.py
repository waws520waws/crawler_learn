
import asyncio
import time
import aiohttp

start_time = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]

async def get_page(url):
    # requests 属于同步模块,所以这里不用
    # async：声明后面跟的是异步操作
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # 注意：获取响应数据之前一定要进行手动挂起
            page = await response.text()
            print(page)

tasks = []
for url in urls:
    xc = get_page(url)
    task = asyncio.ensure_future(xc)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start_time)


