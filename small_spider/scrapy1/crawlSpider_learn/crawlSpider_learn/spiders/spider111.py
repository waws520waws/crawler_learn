import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlSpider_learn.items import CrawlspiderLearnItem, DetailItem

'''
需求：拿到列表页的标题 以及 详情页的标题和介绍
    - 分析1：每一条数据的各项不在同一个页面中，可用请求传参
        - 方法：继承Spider父类，手动编写request，传递item
    - 分析2：继承CrawlSpider父类，自动获取链接，请求数据，解析数据
        - 下面使用此方法
'''

class Spider111Spider(CrawlSpider):
    name = 'spider111'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ivsky.com/tupian/ziranfengguang/']

    # 链接提取器：根据指定规则（allow='正则'）提取start_urls对应页面中的链接
    # 正则只需筛选出需要的链接：如 <a href="/tupian/ziranfengguang/index_2.html" class="page-num">
    links = LinkExtractor(allow=r'index_\d+.html')  # 页码链接

    links_detail = LinkExtractor(allow=r'tupian/[a-z]+_v\d+')  # 详情页链接

    rules = (
        # 规则解析器：将链接提取器提取到的链接请求后的响应数据给parse_item进行解析
        # follow=True：链接提取器提取到的链接links，对links中的链接对应的页面 继续使用相同的正则进行链接提取
        # 不用担心取到相同的链接，scrapy自带过滤器，自动去重
        Rule(links, callback='parse_item', follow=True),

        Rule(links_detail, callback='parse_detail', follow=False),
    )

    ## 【如下两个方法不可以实现请求传参，因为其是继承Spider父类】
    # 可以分别存到两个item中

    # 解析列表页的标题
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[3]/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./p/a/text()')
            item = CrawlspiderLearnItem()
            item['title'] = title
            yield item

    # 解析详情页的标题和介绍
    def parse_detail(self, response):
        pic_title = response.xpath('/html/body/div[3]/div[3]/div[1]/h1/text()')
        pic_content = response.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/p/text()')
        item = DetailItem()
        item['pic_title'] = pic_title
        item['pic_content'] = pic_content
        yield item
