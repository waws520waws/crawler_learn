import scrapy

from apps.items import AppsItem  # 导入item类
import re  # 导入正则表达式类

class AppsSpider(scrapy.Spider):
    name = 'Apps'
    allowed_domains = ['www.coolapk.com']
    start_urls = ['https://www.coolapk.com/apk?p=1']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS" :{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent':'Mozilla/5.0 你的UA'

        }
    }
