# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义属性
    author = scrapy.Field()
    content = scrapy.Field()
    pass
