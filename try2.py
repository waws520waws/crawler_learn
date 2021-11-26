import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True)  # 运行一个无头的浏览器
    page = await browser.newPage()  # 在此浏览器上创建新页面
    await page.goto('https://www.baidu.com')  # 加载一个页面
    # await page.screenshot({'path': 'baidu.png'})  # 把网页生成截图
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())  # 异步