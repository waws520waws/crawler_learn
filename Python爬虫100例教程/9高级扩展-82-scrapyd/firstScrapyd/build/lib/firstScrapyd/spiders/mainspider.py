import scrapy
from firstScrapyd.items import FirstscrapydItem

class MainspiderSpider(scrapy.Spider):
    name = 'mainspider'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://top.baidu.com/buzz?b=1&fr=topindex']

    def parse(self, response):
        title_list = response.xpath("//div[@class='c-single-text-ellipsis']/text()").extract()
        for title in title_list:
            item = FirstscrapydItem()
            item["title"] = title
            yield item
