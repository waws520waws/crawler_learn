import asyncio

import requests


async def get_content(title, cid, book_id):
    url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}'
    params = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }


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
    get_book_id(url, book_id)
