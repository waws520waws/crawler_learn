import asyncio

async def others():
  print('start......')
  await asyncio.sleep(2)
  print('end')
  return '返回值'

async def func():
    print('func()......')
    response1 = await others()
    print(response1)
    response2 = await others()
    print(response2)

asyncio.run(func())