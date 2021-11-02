# -*- coding: UTF-8 -*-

import re  # 正则表达式模块
import threading  # 多线程模块
import time  # 时间模块
import os  # 目录操作模块

import requests

'''
参考：https://blog.csdn.net/hihell/article/details/82490799
需求：爬取图片网站的所有图片
技术：多线程、生产者-消费者模式
'''

all_img_urls = []  # 图片列表页面的数组

g_lock = threading.Lock()  # 初始化一个锁


# 生产者，负责从每个页面提取图片列表链接
class Producer(threading.Thread):

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST': 'www.tupianwangzhan.com'
        }
        global all_urls
        while len(all_urls) > 0:
            '''
            称为'线程同步'：
                对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间
                因为如果多个线程共同对某个数据修改，则可能出现不可预料的结果
            '''
            g_lock.acquire()  # 在访问all_urls的时候，需要使用锁机制
            page_url = all_urls.pop()  # 通过pop方法移除最后一个元素，并且返回该值
            g_lock.release()  # 使用完成之后及时把锁给释放，方便其他线程使用

            try:
                print("分析" + page_url)
                response = requests.get(page_url, headers=headers, timeout=3)
                all_pic_link = re.findall('<a target=\'_blank\' href="(.*?)">', response.text, re.S)
                global all_img_urls

                g_lock.acquire()  # 这里还有一个锁
                all_img_urls += all_pic_link  # 这个地方注意数组的拼接，没有用append直接用的+=也算是python的一个新语法吧
                print(all_img_urls)
                g_lock.release()  # 释放锁

                time.sleep(0.5)
            except:
                pass


# threads= []
# 开启两个线程去访问
for x in range(2):
    t = Producer()
    t.start()
    # threads.append(t)

# for tt in threads:
#     tt.join()

print("进行到我这里了")

pic_links = []  # 图片地址列表


# 消费者
class Consumer(threading.Thread):
    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST': 'www.tupianwangzhan.com'
        }
        global all_img_urls  # 调用全局的图片详情页面的数组
        print("%s is running " % threading.current_thread)
        while len(all_img_urls) > 0:
            g_lock.acquire()
            img_url = all_img_urls.pop()
            g_lock.release()
            try:
                response = requests.get(img_url, headers=headers)
                response.encoding = 'gb2312'  # 由于我们调用的页面编码是GB2312，所以需要设置一下编码
                title = re.search('<title>(.*?) | X图片图</title>', response.text).group(1)
                all_pic_src = re.findall('<img alt=.*?src="(.*?)" /><br />', response.text, re.S)

                pic_dict = {title: all_pic_src}  # python字典
                global pic_links
                g_lock.acquire()
                pic_links.append(pic_dict)  # 字典数组
                print(title + " 获取成功")
                g_lock.release()

            except:
                pass
            time.sleep(0.5)


# 开启10个线程去获取链接
for x in range(10):
    ta = Consumer()
    ta.start()


class DownPic(threading.Thread):

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST': 'www.baidu.com'

        }
        while True:  # 这个地方写成死循环，为的是不断监控图片链接数组是否更新
            global pic_links
            # 上锁
            g_lock.acquire()
            if len(pic_links) == 0:  # 如果没有图片了，就解锁
                # 不管什么情况，都要释放锁
                g_lock.release()
                continue
            else:
                pic = pic_links.pop()
                g_lock.release()
                # 遍历字典列表
                for key, values in pic.items():
                    path = key.rstrip("\\")
                    is_exists = os.path.exists(path)
                    # 判断结果
                    if not is_exists:
                        # 如果不存在则创建目录
                        # 创建目录操作函数
                        os.makedirs(path)

                        print(path + '目录创建成功')

                    else:
                        # 如果目录存在则不创建，并提示目录已存在
                        print(path + ' 目录已存在')
                    for pic in values:
                        filename = path + "/" + pic.split('/')[-1]
                        if os.path.exists(filename):
                            continue
                        else:
                            try:
                                response = requests.get(pic, headers=headers)
                                with open(filename, 'wb') as f:
                                    f.write(response.content)

                            except Exception as e:
                                print(e)
                                pass


# 开启10个线程保存图片
for x in range(10):
    down = DownPic()
    down.start()
