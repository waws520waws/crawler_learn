# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlspiderLearnItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()


class DetailItem(scrapy.Item):
    # define the fields for your item here like:
    pic_title = scrapy.Field()
    pic_content = scrapy.Field()