import scrapy
from learn_scrapy.items import LearnScrapyItem
import pymysql

# 先更改为不遵守
# ROBOTSTXT_OBEY = False

class FirstSpider(scrapy.Spider):
    name = 'first'
    # 允许爬取的域名（如果遇到非该域名的url则爬取不到数据）
    # allowed_domains = ['https://www.qiushibaike.com/']
    # scrapy会自动请求这些url
    start_urls = ['https://www.qiushibaike.com/text/']

    # response为请求得到的响应数据，start_urls有多个就会调用多次此函数
    # 该函数返回值必须为可迭代对象或者NUll
    def parse(self, response):
        # xpath为response中的方法，可以将xpath表达式直接作用于该函数中
        odiv = response.xpath('//div[@class="col1 old-style-col1"]/div')
        print(odiv)
        all_data = []  # 用于存储解析到的数据

        ## 基于终端指令的持久化存储
        # for div in odiv:
        #     # xpath函数返回的为列表，列表中存放的数据为Selector类型的数据。需要调用extract()函数将解析的内容从Selector中取出。
        #     author = div.xpath('.//div[@class="author clearfix"]/a/h2/text()')[0].extract()
        #     content = div.xpath('.//div[@class="content"]/span/text()')[0].extract()
        #     # 提供另外的方法
        #     # div.xpath('//div').extract_first()
        #     # div.xpath('//div').re(r'Name:\s*(.*)')
        #     # div.css('base::attr(href)').extract()
        #     # div.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()  # 选择有”class”元素且结尾为一个数字的链接
        #
        #     dic = {
        #         'author': author,
        #         'content': content
        #     }
        #     all_data.append(dic)
        # return all_data

        ## 基于管道的持久化存储
        for div in odiv:
            # xpath函数返回的为列表，列表中存放的数据为Selector类型的数据。需要调用extract()函数将解析的内容从Selector中取出。
            author = div.xpath('.//div[@class="author clearfix"]/a/h2/text()')[0].extract()
            content = div.xpath('.//div[@class="content"]/span/text()')[0].extract()

            item = LearnScrapyItem()
            # 这里的属性要与item.py中定义属性一致
            item['author'] = author
            item['content'] = content

            yield item  # 将item提交给优先级最高的管道类


