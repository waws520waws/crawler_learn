import scrapy
from all_page_crawl.items import AllPageCrawlItem
'''
需求：爬取某网站的前5页 + 请求传参（传递item对象）
'''

class CrawlManyPageSpider(scrapy.Spider):
    name = 'crawl_many_page'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ivsky.com/tupian/ziranfengguang/']

    # 模板url
    url = 'https://www.ivsky.com/tupian/ziranfengguang/index_%d.html'
    page_num = 2

    # 回调函数接受item，解析详情页
    def crawl_detail(self, response):
        item = response.meta['img_item']  # 调用传递过来的item对象
        img_desc = response.xpath('//div[@class="al_p"]//text()').extract()
        item['img_desc'] = img_desc
        yield item

    ## 解析图片名称
    def parse(self, response):
        img_name = response.xpath('//ul[@class="ali"]/li/p/a/text()').extract()
        print(img_name)
        print('>>>>>>>>>>>>>>>>>>')

        ## 请求传参
        item = AllPageCrawlItem()
        item['img_name'] = img_name

        detail_url = 'https://www.ivsky.com' + response.xpath('//ul[@class="ali"]/li/p/a/@href')

        # 对详情页发请求获取详情页的页面源码数据
        # 手动请求的发送
        # 请求传参：meta={}，可以将meta字典传递给请求对应的回调函数
        yield scrapy.Request(url=detail_url, callback=self.crawl_detail, meta={'img_item': item})

        ## 分页操作
        if self.page_num <= 5:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 递归爬取数据：callback参数的值为回调函数（将url请求后，得到的相应数据继续进行parse解析），递归调用parse函数
            yield scrapy.Request(url=new_url, callback=self.parse)
