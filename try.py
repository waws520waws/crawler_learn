import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])  # 运行一个无头的浏览器,headless是否输出网页源码

    # 打开新的标签页
    page = await browser.newPage()

    # 设置视图大小
    await page.setViewport({'width': 1366, 'height': 768})

    # 设置UserAgent
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')

    # 访问页面
    response = await page.goto('https://www.baidu.com')

    # status
    print(response.status)


    # 定位元素
    # 1、只定位一个元素（css选择器）
    # element = await page.querySelector('#s-top-left > a')
    # 2、css选择器
    # elements = await page.querySelectorAll('#s-top-left > a:nth-child(2n)')
    # 3、xpath
    # elements = await page.xpath('//div[@id="s-top-left"]/a[1]/text()')
    # print(elements)
    # for element in elements:
    #     print(await (await element.getProperty('textContent')).jsonValue())  # 获取文本内容
    #     print(await (await element.getProperty('href')).jsonValue())  # 获取href属性

    await asyncio.sleep(5)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())  # 异步
# asyncio.run(main())