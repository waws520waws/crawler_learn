import re

import scrapy
from kuAn.items import KuanItem


class KuanspiderSpider(scrapy.Spider):
    name = 'kuAnSpider'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.coolapk.com/apk/']

    base_url = 'https://www.coolapk.com/apk?p={}'

    # custom_settings 第一次出现，目的是修改默认 setting.py 文件中的配置
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 你的UA'

        }
    }

    def parse(self, response):
        print(response.url)
        list_items = response.css(".app_left_list>a")
        for item in list_items:
            url = item.css("::attr('href')").extract_first()  # [标签]::属性或文本

            url = response.urljoin(url)  # 自己的理解：会自动获取请求的链接的主域名url，然后与参数中的url拼接

            yield scrapy.Request(url, callback=self.parse_url)

        next_page = response.css('.pagination li:nth-child(8) a::attr(href)').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url, callback=self.parse)

    def parse_url(self, response):
        item = KuanItem()

        item["title"] = response.css(".detail_app_title::text").extract_first()
        info = self.getinfo(response)

        item['volume'] = info[0]
        item['downloads'] = info[1]
        item['follow'] = info[2]
        item['comment'] = info[3]

        item["tags"] = self.gettags(response)
        item['rank_num'] = response.css('.rank_num::text').extract_first()
        item['rank_num_users'] = response.css('.apk_rank_p1::text').re("共(.*?)个评分")[0]
        item["update_time"], item["rom"], item["developer"] = self.getappinfo(response)

        yield item

    def getinfo(self, response):
        info = response.css(".apk_topba_message::text").re("\s+(.*?)\s+/\s+(.*?)下载\s+/\s+(.*?)人关注\s+/\s+(.*?)个评论.*?")
        return info

    def gettags(self, response):
        tags = response.css(".apk_left_span2")
        tags = [item.css('::text').extract_first() for item in tags]

        return tags

    def getappinfo(self, response):
        # app_info = response.css(".apk_left_title_info::text").re("[\s\S]+更新时间：(.*?)")
        body_text = response.body_as_unicode()

        update = re.findall(r"更新时间：(.*)?[<]", body_text)[0]
        rom = re.findall(r"支持ROM：(.*)?[<]", body_text)[0]
        developer = re.findall(r"开发者名称：(.*)?[<]", body_text)[0]
        return update, rom, developer
