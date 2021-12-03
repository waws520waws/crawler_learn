import scrapy
from juejin.items import JuejinItem

class JuejinspiderSpider(scrapy.Spider):
    name = 'juejinSpider'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://juejin.cn/user/712139233835879/following']

    base_url = 'https://juejin.cn/user/{}/following'

    def parse(self, response):
        print('is crawling:->', response.url)

        username = response.xpath('//h1/text()').extract_first()
        position = response.xpath('//div[@class="position"]/span//text()').extract()
        # print(position)
        position = ''.join(position)
        liked = response.xpath('//span[contains(text(), "文章被点赞")]/span/text()').extract_first()
        read = response.xpath('//span[contains(text(), "文章被阅读")]/span/text()').extract_first()
        dig_value = response.xpath('//span[contains(text(), "掘力值")]/span/text()').extract_first()

        item = JuejinItem()
        item['username'] = username
        item['position'] = position if position else ''
        item['liked'] = liked
        item['read'] = read
        item['dig_value'] = dig_value
        yield item

        li_list = response.xpath('//ul[@class="tag-list"]/li')
        for li in li_list:
            userID = li.xpath('.//a[@class="username"]/@href').extract_first()
            userID = userID.split('user/')[1]
            yield scrapy.Request(self.base_url.format(userID), callback=self.parse)


