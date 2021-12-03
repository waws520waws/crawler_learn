# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JuejinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    username = scrapy.Field()
    position = scrapy.Field()
    liked = scrapy.Field()
    read = scrapy.Field()
    dig_value = scrapy.Field()
