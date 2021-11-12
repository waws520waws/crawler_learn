import threading
from queue import Queue
import requests
import time


CRAWL_EXIT = False  # 标识爬虫的状态
class ThreadCrawl(threading.Thread):

    def __init__(self, thread_name, page_queue, data_queue):
        # threading.Thread.__init__(self)
        # 调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        self.threadName = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue

    def run(self):
        print(self.threadName + ' 启动************')
        while not CRAWL_EXIT:
            try:
                global tag, url, headers, img_format  # 把全局的值拿过来
                # 队列为空 产生异常
                page = self.page_queue.get(block=False)  # 从里面获取值
                spider_url = url_format.format(tag, page, 100)  # 拼接要爬取的URL
                print(spider_url)
            except:
                break

            timeout = 4  # 合格地方是尝试获取3次，3次都失败，就跳出
            while timeout > 0:
                timeout -= 1
                try:
                    with requests.Session() as s:
                        response = s.get(spider_url, headers=headers, timeout=3)
                        json_data = response.json()
                        if json_data is not None:
                            imgs = json_data["postList"]
                            for i in imgs:
                                imgs = i["images"]
                                for img in imgs:
                                    img = img_format.format(img["user_id"], img["img_id"])
                                    self.data_queue.put(img)  # 捕获到图片链接，之后，存入一个新的队列里面，等待下一步的操作

                    break

                except Exception as e:
                    print(e)

            if timeout <= 0:
                print('time out!')


DOWN_EXIT = False
class ThreadDown(threading.Thread):
    def __init__(self, thread_name, data_queue):
        super(ThreadDown, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue

    def run(self):
        print(self.thread_name + ' 启动************')
        while not DOWN_EXIT:
            try:
                img_link = self.data_queue.get(block=False)
                self.write_image(img_link)
            except Exception as e:
                pass

    def write_image(self, url):

        with requests.Session() as s:
            response = s.get(url, timeout=3)
            img = response.content   # 获取二进制流

        try:
            file = open('image/' + str(time.time())+'.jpg', 'wb')
            file.write(img)
            file.close()
            print('image/' + str(time.time())+'.jpg 图片下载完毕')

        except Exception as e:
            print(e)
            return


def main():
    ## 1、采集图片 >>>>>>>>>>>>>>>>>>
    # 声明一个队列，使用循环在里面存入100个页码
    page_queue = Queue(100)
    for i in range(1, 101):
        page_queue.put(i)

    # 采集结果(等待下载的图片地址)
    data_queue = Queue()

    # 记录线程的列表
    thread_crawl = []
    # 每次开启4个线程
    craw_list = ['采集线程1号', '采集线程2号', '采集线程3号', '采集线程4号']
    for thread_name in craw_list:
        c_thread = ThreadCrawl(thread_name, page_queue, data_queue)
        c_thread.start()
        thread_crawl.append(c_thread)

    # 等待page_queue队列为空，也就是等待之前的操作执行完毕
    while not page_queue.empty():
        pass

    # 如果page_queue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True

    ## 2、下载图片 >>>>>>>>>>>>>>>>>>
    for thread in thread_crawl:
        thread.join()
        print("抓取线程结束")

    thread_image = []
    image_list = ['下载线程1号', '下载线程2号', '下载线程3号', '下载线程4号']
    for thread_name in image_list:
        Ithread = ThreadDown(thread_name, data_queue)
        Ithread.start()
        thread_image.append(Ithread)

    while not data_queue.empty():
        pass

    global DOWN_EXIT
    DOWN_EXIT = True

    for thread in thread_image:
        thread.join()
        print("下载线程结束")


if __name__ == '__main__':
    main()
