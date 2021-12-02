# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BliblicommentsItem(scrapy.Item):
    # define the fields for your item here like:
    uname = scrapy.Field()
    content = scrapy.Field()
    mid = scrapy.Field()
    likes = scrapy.Field()

