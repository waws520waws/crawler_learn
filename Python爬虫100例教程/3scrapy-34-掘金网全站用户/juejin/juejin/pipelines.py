# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class JuejinPipeline:
    def __init__(self):
        self.f = open('./juejinUsrInfo.csv', 'a+', encoding='utf-8')
        self.write = csv.writer(self.f)

    def open_spider(self, spider):
        print('open spider:')

    def process_item(self, item, spider):
        try:
            if item:
                row = (item['username'], item['position'], item['liked'], item['read'], item['dig_value'])
                self.write.writerow(row)
        except Exception as e:
            print(e)

        return item

    def close_spider(self, spider):
        self.f.close()
        print('close spider !!!')