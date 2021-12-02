# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class BliblicommentsPipeline:
    def __init__(self):
        cli = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = cli['eg_100_db']

    def open_spider(self, spider):
        print('open spider:')

    def process_item(self, item, spider):
        data = {
            'uname': item['uname'],
            'content': item['content'],
            'mid': item['mid'],
            'likes': item['likes']
        }
        self.db['data32'].insert_one(data)

        return item

    def close_spider(self, spider):
        print('close spider!!!')
