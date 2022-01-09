import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from distributed_crawl.items import DistributedCrawlItem
from scrapy_redis.spiders import RedisCrawlSpider

class Spider222Spider(RedisCrawlSpider):
    name = 'spider222'
    # allowed_domains = ['www.ivsky.com']
    # start_urls = ['https://www.ivsky.com/tupian/ziranfengguang/']

    # 调度器名称
    redis_key = 'spider222:start_urls'  # 一般取名为 '爬虫文件名:start_urls'

    links = LinkExtractor(allow=r'index_\d+.html')

    rules = (
        Rule(links, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[3]/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./p/a/text()')
            item = DistributedCrawlItem()
            item['title'] = title
            yield item
