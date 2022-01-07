# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class CsdnDownFileItem(scrapy.Item):
    # define the fields for your item here like:
    file_id = scrapy.Field()
    title = scrapy.Field()
    source_url =scrapy.Field()
    pass

