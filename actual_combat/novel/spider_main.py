import asyncio
import aiohttp
import requests
import aiofiles
import json
'''
需求：抓取百度小说中 西游记 的全部章节内容
参考：https://www.bilibili.com/video/BV1i54y1h75W?p=67
'''

async def get_content(title, cid, book_id):
    params = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    params = json.dumps(params)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={params}'
    # 外层异步，内层若是io操作，则要异步？
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page = await response.json()
            # 将novel_content文件标记为exclusion，快，不卡，但。。。
            file = './novel_content/%s' % title
            async with aiofiles.open(file, 'w', encoding='utf-8') as f:
                content = page['data']['novel']['content']
                await f.write(content)


async def get_book_id(url, book_id):
    req = requests.get(url)
    page = req.json()
    tasks = []
    for item in page['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(get_content(title, cid, book_id))
    # 等价于(但是是使用在普通函数中，get_book_id函数就不用加async)
    # asyncio.run(asyncio.wait(tasks))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'

    asyncio.run(get_book_id(url, book_id))
