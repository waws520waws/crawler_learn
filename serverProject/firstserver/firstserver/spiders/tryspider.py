import scrapy
from firstserver.items import FirstserverItem

class TryspiderSpider(scrapy.Spider):
    name = 'tryspider'
    allowed_domains = ['www.xx.com']
    start_urls = ['http://top.baidu.com/buzz?b=1&fr=topindex']

    def parse(self, response):
        title_list = response.xpath("//div[@class='c-single-text-ellipsis']/text()").extract()
        for title in title_list:
            item = FirstserverItem()
            item["title"] = title
            print(item)
            print(type(item))
            yield item
            break
