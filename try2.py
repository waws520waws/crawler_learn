import scrapy
from baiduindex.items import BaiduindexItem

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['top.baidu.com']
    start_urls = ['http://top.baidu.com/buzz?b=1&fr=topindex']

    def parse(self, response):
        title_list = response.xpath("//a[@class='list-title']/text()").extract()
        for title in title_list:
            item = BaiduindexItem()
            item["title"] = title
            yield item
