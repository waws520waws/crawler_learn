#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2021-11-29 11:55:32
# Project: reeoo

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    # @every(minutes=24 * 60)  # 通知 scheduler（框架的模块） 每天运行一次
    # def on_start(self):  # 程序的入口
    #     self.crawl('https://reeoo.com/', callback=self.index_page)  # url 为爬取地址，callback 为抓取到数据response后的回调函数

    @config(age=10 * 24 * 60 * 60)  # 设置任务的有效期限，在这个期限内目标爬取的网页被认为不会进行修改
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():  # response.doc 为 pyquery 对象，抓取对应标签的数据
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)  # 设定任务优先级
    def detail_page(self, response):
        return {  # 返回一个 dict 对象，结果会自动保存到默认的 resultdb 中，也可以通过重写on_result(self, result)方法来将结果数据存储到指定的数据库
            "url": response.url,
            "title": response.doc('title').text(),
        }


