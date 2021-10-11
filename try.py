import asyncio

class AsyncContextManager:
    def __init__(self):
        self.conn = conn
    async def do_something(self):
      # 异步操作数据库
        return 666
    async def __aenter__(self):
      # 异步连接数据库
        self.conn = await asyncio.sleep(1)
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        await asyncio.sleep(1)

async def func():
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)