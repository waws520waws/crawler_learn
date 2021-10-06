# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GetUpdateDataPipeline:
    conn = None

    # 可通过spider使用爬虫文件的属性和方法
    def open_sipder(self, spider):
        self.conn = spider.conn

    def process_item(self, item, spider):
        detail_data = {
            'pic_title': item['pic_title'],
            'pic_content': item['pic_content']
        }
        # 爬取到的数据存入redis的一个列表中
        self.conn.lpush('name_of_list', detail_data)
        return item
