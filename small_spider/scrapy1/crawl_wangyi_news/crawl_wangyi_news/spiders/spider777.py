import scrapy
from selenium import webdriver
from crawl_wangyi_news.items import CrawlWangyiNewsItem
'''
需求：爬取网易新闻‘国内’，‘国际’，‘军事’板块下的新闻标题和内容
'''

class Spider777Spider(scrapy.Spider):
    name = 'spider777'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']

    # 【这些板块下是动态数据】不能直接请求，这里用到’下载中间件‘拦截响应对象，并使用selenium重新请求动态数据
    models_urls = []  # 存储‘国内’，‘国际’，‘军事’板块的url

    # 实例化一个浏览器对象
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:\pycharmProject\crawler_learn\small_spider\selenium\chromedriver.exe')

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        nums = [3, 4, 6]
        for num in nums:
            model_url = li_list.xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        # 依次对每一个板块的url进行请求
        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    # 解析板块下的新闻标题以及详情页的url
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/@text()').extract_first()
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = CrawlWangyiNewsItem()
            item['title'] = title

            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

    # 解析新闻内容
    def parse_detail(self, response):
        content = response.xpath('//*[@id="content"]/div[2]//text()')
        content = ''.join(content)
        item = response.meta['item']  # 接收传递过来的item对象
        item['content'] = content
        yield item  # 提交给管道，再进行持久化存储

    # 只在爬虫结束时调用一次
    def closed(self, spider):
        self.driver.quit()
