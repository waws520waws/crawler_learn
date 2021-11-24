from requests_html import AsyncHTMLSession
import pymongo

'''
- 需求：51CTO学院IT技术课程
- 技术：requests_html(异步请求、解析)
'''

asysession = AsyncHTMLSession()
url = "https://edu.51cto.com/courselist/index-p{}.html?edunav="

cli = pymongo.MongoClient('mongodb://localhost:27017/')
db = cli['eg_100_db']


def get_item(html):
    li_list = html.xpath('//ul[@class="Courselist-common clearfix2"]/li')
    if li_list:
        for li in li_list:
            try:
                title = li.xpath('.//div[@class="title"]/text()')[0]
                course_length = li.xpath('.//div[@class="num clearfix2"]/span[1]//text()')[0]
                numbers = li.xpath('.//div[@class="num clearfix2"]/span[2]//text()')[0]
                score = li.xpath('.//span[@class="score fl"]/text()')[0]
                teacher = li.xpath('.//span[@class="fr name"]/text()')[0]
                price = li.xpath('.//span[@class="new fl"]//text()')[1]
                dic = {
                    'title': title,
                    'course_length': course_length,
                    'numbers': numbers,
                    'score': score,
                    'teacher': teacher,
                    'price': price
                }
                db['data_19'].insert_one(dic)
                print('success!!!')

            except Exception:
                pass


async def getHtml():
    for i in range(1, 2):
        res = await asysession.get(url.format(i))
        get_item(res.html)


if __name__ == '__main__':
    asysession.run(getHtml)  ## run的是函数名，不穿参数