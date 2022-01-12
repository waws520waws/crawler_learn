import scrapy
from demo78.items import Demo78Item

import sys
sys.path.append('../..')
from bloomcheck import BloomCheck

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
