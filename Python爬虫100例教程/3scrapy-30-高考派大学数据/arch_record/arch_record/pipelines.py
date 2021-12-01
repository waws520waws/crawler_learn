# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class ArchRecordPipeline:
    def __init__(self):  # 执行一次
        print('init 被执行了！！！')
        cli = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = cli['eg_100_db']

    # 重写父类的一个方法：该方法只在爬虫开始的时候被调用一次
    def open_spider(self, spider):
        print('开启爬虫：')

    # 该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):  # 执行多次
        print('process_item被执行了！！！')
        title = item['title']
        author = item['author']
        date = item['date']
        self.db['data30'].insert_one({'title': title, 'author': author, 'date':date})

        return item

    # 重写父类的一个方法：该方法只在爬虫结束的时候被调用一次
    def close_spider(self, spider):
        print('爬虫结束！！！')
