import requests_html
import threading
import queue


url = 'https://www.freetechbooks.com/topics'
detail_url_queue = queue.Queue(maxsize=100)
class ThreadCrawl(threading.Thread):

    def __init__(self, page_queue):
        threading.Thread.__init__(self)
        self.page_queue = page_queue


    def run(self):
        global url
        global detail_url_queue
        while True:
            try:
                page_num = self.page_queue.get(block=False)
                list_url = f'{url}?page={page_num}'
                print(list_url)
            except:
                print('page_queue 一滴都没有了！！！')
                break

            try:
                session = requests_html.HTMLSession()
                res = session.get(list_url)
                hrefs = res.html.xpath("//p[@class='media-heading lead']/a/@href")

                for href in hrefs:
                    detail_url_queue.put(href)
            except Exception as e:
                print('ThreadCrawl出错啦！！！', e)


data_info = []
class ThreadDown(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        global data_info
        global detail_url_queue
        while True:
            try:
                detail_url = detail_url_queue.get(block=False)

            except:
                print('detail_url_queue 一滴都没有了！！！')
                break

            try:
                session = requests_html.HTMLSession()
                res = session.get(detail_url)
                title = res.html.xpath('//p[@class="media-heading lead"]/text()')[0]
                pdf_link = res.html.xpath('//div[@id="srvata-content"]//a/@href')[0]

                if pdf_link.endswith('.pdf'):
                    data_info = {'title': title, 'pdf_link': pdf_link}

            except Exception as e:
                print('ThreadDown出错啦！！！', e)

        print(data_info)


def main():
    page_queue = queue.Queue(maxsize=10)
    for i in range(2):
        page_queue.put(i+1)

    for i in range(2):
        tt = ThreadCrawl(page_queue)
        tt.start()
        tt.join()

    for i in range(3):
        tt = ThreadDown()
        tt.start()
        tt.join()


if __name__ == '__main__':
    main()