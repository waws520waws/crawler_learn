#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2021-11-30 14:55:25
# Project: spider100eg_27_phoneAPPdata

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.liqucn.com/rj/new/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        etree = response.etree
        start_page = etree.xpath('//a[text()="2"]/@href')[0]
        start_page = start_page.split('=')[1]
        end_page = etree.xpath('//a[contains(text(), "尾页")]/@href')[0]
        end_page = end_page.split('=')[1]
        for i in range(16138, 16141):
            self.crawl(f'https://www.liqucn.com/rj/new/?page={i}', method='GET', callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        etr = response.etree
        li_list = etr.xpath('//ul[@class="tip_blist"]/li')
        app_data = []
        for li in li_list:
            app_name = li.xpath('.//span//text()')[0]
            date = li.xpath('.//i[1]/text()')[0]
            category = li.xpath('.//i[2]/text()')[0]
            app_data.append({
                "app_name": app_name,
                "date": date,
                'category': category
            })

        return app_data

    def on_result(self, result):
        if result:
            cli = pymongo.MongoClient('mongodb://localhost:27017')
            db = cli['eg_100_db']
            db['data27'].insert_many(result)
