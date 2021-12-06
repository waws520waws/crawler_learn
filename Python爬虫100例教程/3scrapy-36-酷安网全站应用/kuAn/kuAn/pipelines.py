# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class KuanPipeline(object):

    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    # from_crawler 是一个类方法，在初始化的时候，从 setting.py 中读取配置
    @classmethod
    def from_crawler(cls, crawler):
        return cls(     # cls代表的是类的本身，相对应的self则是类的一个实例对象
            mongo_url=crawler.settings.get("MONGO_URL"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        try:
            self.client = pymongo.MongoClient(self.mongo_url)
            self.db = self.client[self.mongo_db]

        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        name = item.__class__.__name__

        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
