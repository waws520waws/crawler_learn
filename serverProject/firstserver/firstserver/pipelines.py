# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class FirstserverPipeline:
    def __init__(self):
        client = pymongo.MongoClient('47.101.158.121', 27017)
        self.db = client['testdb']
        self.db.authenticate('jieyang', '970706')

    def process_item(self, item, spider):
        if item:
            self.db['mytable1'].insert_one(dict(item))
        return item
