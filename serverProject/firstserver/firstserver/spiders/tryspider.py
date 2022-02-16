import scrapy
from firstserver.items import FirstserverItem
from aroay_cloudscraper import CloudScraperRequest

class TryspiderSpider(scrapy.Spider):
    name = 'tryspider'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.today.ng/sport/basketball']
    base_url = 'https://www.today.ng/sport/basketball'

    def start_requests(self):
        yield CloudScraperRequest(self.base_url, callback=self.parse, dont_filter=True, cookies={"over18":"1"},timeout=5)

    def parse(self, response):
        title_list = response.xpath("//h2/a/text()").extract()
        for title in title_list:
            item = FirstserverItem()
            item["title"] = title
            print(item)
            print(type(item))
            yield item
