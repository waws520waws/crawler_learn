'''
- 需求：微医挂号网医生数据
- 技术：pyppeteer（自动化 + asyncio）
(此案例在xpath解析数据时未成功)
'''


import pyppeteer
import asyncio
import pymongo

cli = pymongo.MongoClient('mongodb://localhost:27017/')
db = cli['eg_100_db']


async def getInfo(page):

    li_list = await page.xpath('//div[@class="g-doctor-items to-margin"]/ul/li')
    print(li_list)
    for li in li_list:
        element1 = await li.querySelector('dl dt a')
        name = await (await element1.getProperty('textContent')).jsonValue()
        element2 = await li.querySelector('dl dt')
        position = await (await element2.getProperty('textContent')).jsonValue()
        dic = {
            'name': name,
            'position': position
        }
        db['data_24'].insert_one(dic)
        print(dic)


async def getHtml(url, browser):

    page = await browser.newPage()
    response = await page.goto(url)
    if response.status == 200:
        await getInfo(page)


async def main():
    baseurl = 'https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90/p{}'
    browser = await pyppeteer.launch()
    tasks = []
    for i in range(1, 3):
        tasks.append(getHtml(baseurl.format(i), browser))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())