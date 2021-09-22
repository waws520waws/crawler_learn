# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LearnScrapyPipeline:

    def __init__(self):
        self.fp = None  # 定义一个文件描述符属性

    # 重写父类的一个方法：该方法只在爬虫开始的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫！！！')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')


    # 专门用来处理item类型的对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收一个item就会被调用一次
    # 因为该方法会被执行调用多次，所以文件的开启和关闭操作写在了另外两个只会各自执行一次的方法中。
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+'+'+content+'\n')
        return item  # 会将item传递给下一个即将被执行的管道类

    # 重写父类的一个方法：该方法只在爬虫结束的时候被调用一次
    def close_spider(self, spider):
        self.fp.close()
        print('结束爬虫！！！')


class DoublekillPipeline_db(object):
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            'localhost',
            'db_name',
            'user',
            'password',
            port='',
            chardet='utf-8'
        )

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into XXX values("%s", "%s")'%(item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()