import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Spider111Spider(CrawlSpider):
    name = 'spider111'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/supervise']

    # 链接提取器：根据指定规则（allow='正则'）提取start_urls对应页面中的链接
    # 正则只需筛选出需要的链接：如 <a href="/political/index/supervise?page=2" class="page-num">
    links = LinkExtractor(allow=r'supervise?page=\d+')

    rules = (
        Rule(links, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(response)
        # return item
