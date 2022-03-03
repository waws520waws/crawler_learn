import scrapy
from demo78.items import Demo78Item

import sys
sys.path.append('../..')
from bloomcheck import BloomCheck

'''
注意点
    在此案例中： BloomFilter 是通过读写文件的方式进行去重，如果你编写多进程或者多线程爬虫，使用的时候需要添加互斥和同步条件，
      还有 BloomFilter 涉及文件I/O操作，注意批量写入和批量读取，否则效率会有很大的影响。
'''

class BfilterSpider(scrapy.Spider):
    name = 'bfilter'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://xz.aliyun.com/']

    def parse(self, response):
        print(response.text)
        li_list = response.xpath("//a[@class='topic-title']")
        bf = BloomCheck()
        print(li_list)
        for li in li_list:
            de_item = Demo78Item()
            title = li.xpath("./text()").extract_first().strip()
            # 判断title是否在bf文件中，如果不在，返回新数据
            if bf.process_item(title):
                de_item['title'] = title
                de_item['url'] = "https://xz.aliyun.com" + li.xpath("./@href").extract_first()
                yield de_item
            else:
                print(f"--{title}--数据已经存在，不进行添加")

        # 保存数据
        bf.save_bloom_file()
