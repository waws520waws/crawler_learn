import scrapy


class SuduSpider(scrapy.Spider):
    name = 'sudu'
    allowed_domains = ['www.xx.com']
    start_urls = ['https://www.ivsky.com/tupian/index_1.html', 'https://www.ivsky.com/tupian/index_2.html',
                  'https://www.ivsky.com/tupian/index_3.html', 'https://www.ivsky.com/tupian/index_4.html'
                  'https://www.ivsky.com/tupian/index_5.html', 'https://www.ivsky.com/tupian/index_6.html'
                  'https://www.ivsky.com/tupian/index_7.html', 'https://www.ivsky.com/tupian/index_8.html'
                  'https://www.ivsky.com/tupian/index_9.html', 'https://www.ivsky.com/tupian/index_10.html'
                  'https://www.ivsky.com/tupian/index_11.html', 'https://www.ivsky.com/tupian/index_12.html']

    def parse(self, response):
        print(response.url)
