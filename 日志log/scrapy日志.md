- 【参考官方文档】https://www.osgeo.cn/scrapy/topics/logging.html
- 在 蜘蛛文件中：
  - 方法1：
     ```python
     import scrapy
     from scrapy import Request
     import traceback
    
     class MySpider(scrapy.Spider):
    
         name = 'myspider'
         start_urls = ['https://scrapy.org']
    
         def parse(self, response):
             yield Request(url='', callback=self.parse_detail, errback=self.err_back)
             self.logger.info('Parse function called on %s', response.url)
    
         def parse_detail(self):
             pass
         def err_back(self, response):
             self.logger.info(response.url, traceback.format_exc())
     ```

  - 方法2：
    ```python
    import logging
    import scrapy
    
    logger = logging.getLogger('mycustomlogger')
    
    class MySpider(scrapy.Spider):
    
        name = 'myspider'
        start_urls = ['https://scrapy.org']
    
        def parse(self, response):
            logger.info('Parse function called on %s', response.url)
    ```
    
- 在 settings.py 文件中
```python
LOG_ENABLED = True      # 是否启动日志记录，默认True
LOG_ENCODING = 'UTF-8'  # 编码方式
LOG_FILE_APPEND = True  # 已追加的方式
LOG_FILE = 'TEST1.LOG'  # 日志输出文件（一般格式为：name_date.log），如果为NONE，就打印到控制台
LOG_LEVEL = 'INFO'      # 日志级别，默认debug
LOG_FORMAT              # 日志格式
LOG_DATEFORMAT          # 日志日期格式
LOG_STDOUT              # 日志标准输出，默认False，如果True所有标准输出都将写入日志中，比如代码中的print输出也会被写入到文件
LOG_SHORT_NAMES         # 短日志名，默认为false，如果为True将不输出组件名 
```