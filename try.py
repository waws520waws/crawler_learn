# -*- coding: UTF-8 -*-
import requests  # 网络请求模块
import random  # 随机模块
import re  # 正则表达式模块
import time  # 时间模块
import threading  # 线程模块
import pymongo as pm   #mongodb模块

class Config():
    def getHeaders(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "其它 UserAgent "
        ]
        UserAgent = random.choice(user_agent_list)
        headers = {'User-Agent': UserAgent}
        return headers


# 起始种子地址
urls = ["https://douge2013.zcool.com.cn/follow?condition=0&p=1"]
index = 0  # 索引
g_lock = threading.Lock()  # 初始化一个锁


 # 获取连接
# client = pm.MongoClient('127.0.0.1', 27017)  # 端口号是数值型
#
# # 连接目标数据库
# db = client.zcool
#
# # 数据库用户验证
# db.authenticate("zcool", "zcool")

# 生产者
class Producer(threading.Thread):

    def run(self):
        print("线程启动...")
        headers = Config().getHeaders()
        print(headers)
        global urls
        global index
        while True:
            g_lock.acquire()
            if len(urls) == 0:
                g_lock.release()
                continue
            page_url = urls.pop()
            g_lock.release()  # 使用完成之后及时把锁给释放，方便其他线程使用
            response = ""
            try:
                response = requests.get(page_url, headers=headers, timeout=5)

            except Exception as http:
                print("生产者异常")
                print(http)
                continue
            content = response.text

            rc = re.compile(
                r'<a href="(.*?)" title=".*?" class="avatar" target="_blank" z-st="member_content_card_1_user_face">')
            follows = rc.findall(content)
            # print(follows)
            fo_url = []
            threading_links_2 = []
            print('this is follows:>>>>>>>>>>>>>>')
            print(follows)
            for u in follows:
                # 生成关注列表地址
                this_url = "%s/follow?condition=0&p=1" % u
                g_lock.acquire()
                index += 1
                g_lock.release()
                fo_url.append({"index": index, "link": this_url})
                threading_links_2.append(this_url)

            g_lock.acquire()
            urls += threading_links_2
            g_lock.release()
            # print(fo_url)
            # try:
            #     db.text.insert_many(fo_url,ordered=False )
            # except:
            #     continue

if __name__ == "__main__":
    p = Producer()
    p.start()
