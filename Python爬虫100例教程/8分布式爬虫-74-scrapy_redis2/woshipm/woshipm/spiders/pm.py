'''
分布式爬取 '人人都是产品经理' 网站 http://www.woshipm.com/category/pmd
'''

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class PmSpider(RedisCrawlSpider):
    name = 'pm'
    # allowed_domains = ['www.xx.com']
    # start_urls = ['http://www.woshipm.com/category/pmd']

    redis_key = 'pm:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'pmd/page/\d+'), callback='parse_item', follow=True),  # 因为是元祖，逗号不可省略
    )

    def parse_item(self, response):
        articles = response.xpath("//div[contains(@class, 'home--list')]/article")
        for article in articles:
            item = {}
            item['title'] = article.xpath('.//h2/a/text()').get()
            item['name'] = article.xpath('.//div[contains(@class, "author")]/a/text()').get()
            yield item
