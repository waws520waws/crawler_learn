import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from get_update_data.items import GetUpdateDataItem
from redis import Redis

'''
需求：拿到列表页的标题 以及 详情页的标题和介绍
    - 分析1：每一条数据的各项不在同一个页面中，可用请求传参
        - 方法：继承Spider父类，手动编写request，传递item
    - 分析2：继承CrawlSpider父类，自动获取链接，请求数据，解析数据
        - 下面使用此方法
'''

class Spider333Spider(CrawlSpider):
    name = 'spider333'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ivsky.com/tupian/ziranfengguang/']

    # 链接提取器：根据指定规则（allow='正则'）提取start_urls对应页面中的链接
    # 正则只需筛选出需要的链接：如 <a href="/tupian/ziranfengguang/index_2.html" class="page-num">
    links = LinkExtractor(allow=r'index_\d+.html')  # 页码链接

    rules = (
        # 规则解析器：将链接提取器提取到的链接请求后的响应数据给parse_item进行解析
        # follow=True：链接提取器提取到的链接links，对links中的链接对应的页面 继续使用相同的正则进行链接提取
        # 不用担心取到相同的链接，scrapy自带过滤器，自动去重
        Rule(links, callback='parse_item', follow=True),
    )

    conn = Redis(host='127.0.0.1', port=6379)

    # 解析每一个页面对应的页面中的详情页的url
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[3]/div[2]/ul/li')
        for li in li_list:
            detail_url = li.xpath('./p/a/@href').extract_first()

            # 将详情页的url存入redis的set中(key:urls_set_name； value:一个集合，detail_url存储在这个集合中)
            ex = self.conn.sadd('urls_set_name', detail_url)

            # 若redis中没有此url，则成功存入set中，返回1，表示还未爬取过，否则返回0
            if ex == 1:
                print('该url没有被爬过，可以进行数据的爬取')
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)
            else:
                print('数据还没更新，暂无新数据可爬取')

    # 解析详情页的标题和介绍，并持久化存储
    def parse_detail(self, response):
        pic_title = response.xpath('/html/body/div[3]/div[3]/div[1]/h1/text()')
        pic_content = response.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/p/text()')
        item = GetUpdateDataItem()
        item['pic_title'] = pic_title
        item['pic_content'] = pic_content
        yield item
