# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class Demo78SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Demo78DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = {'cna': 'xmRgGWVKkH4CAavZXPMR01qy', 'aliyun_choice': 'CN', 'isg': 'BBYWvaHvayCug18-AXrnBG1tZ8oYt1rx6qqmb4B_AvmUQ7bd6EeqAXyy29-va1IJ', 'l': 'eBriSdccgcekV91xBOfwourza77OSIRAguPzaNbMiOCPOv1B5StdW6dfouT6C3GVhsHMR3ugb52QBeYBc7F-nxvtGwBLE8Dmn', 'tfstk': 'c52PBbg_Sv4bgRDC6YMFNtUzOwERC-U3yKuqZ77K5agFaQLm-u5crenDs6iqzn8nZ', 'acw_tc': '2f624a3f16419721281801159e4ca0a4738b6c4e3f63d90d29c91043433d9e', 'acw_sc__v2': '61de81a0890653abc057ad827fb5be09fa8cde18', 'UM_distinctid': '17e4d2a5e9ccbd-08fd5a3c70839c-36657407-384000-17e4d2a5e9d12b2', 'CNZZDATA1260716569': '597458352-1641968087-https%3A%2F%2Fxz.aliyun.com%2F|1641968087', '_uab_collina': '164197212982450397524713', 'ssxmod_itna': 'eqGOBK7KAIkDkbDXDnQmidYvqiIrvK2ux9R5KDsqdbDSxGKidDqxBmmQPDteb1eSjG0UqEKtrBq4LAihgDviV7W90xEmPZeKoD84i7DKqibDCqD1D3qDkb9oxiiDGktkcDD2dFS9aVw+WSG4olEqBF7peK75=z3h5YCD=F7v4Dox=mYhqY0rNo7xoVE04xDfdpAP3eD=', 'ssxmod_itna2': 'eqGOBK7KAIkDkbDXDnQmidYvqiIrvK2ux9R5ikA1zDl=miDjb5DtNRNqc8c16ubYw4i8qs=l7iOciziKj+qAYdr28g3frEjvevrpBGCiHGebaEGdSp=y9uGyZ=HCsosyzdD6nxNV2FGdxo8X24q0m3l0wQW2erejKZTA534r5P8251li/zi0Bb0RvSqLq8riqPnQhQmfFpOcwCP67MuN+lLX6j8j/lCKqsR35v6015Gi/ARi=OFFpkjOn3mSvyLFVQdMAq+XmHLNXg8X6UkNCjWBpOVAsH/HeVcusu6Y5c=88pO=VFTYcq3O2NxLs5hb5xF3WK2wTwgOaSY44dy2ToC1qm4IOK2xsijYLr7GjwpMzKuNA4pE27NT7rbF0CNRWN4LIRSIEdd4qdGDoX8YADDw2D5nm7ni4jPYYA+UwFGnqCwCAhuaw8QpF=w8AnUWD8iDHlciQItmGpUDpbGHQI1Yeu/m8jD=DGcDG7LpDdG4IaqqDY17eXiqdiDD'}

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
