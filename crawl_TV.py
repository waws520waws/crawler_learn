import requests
from lxml import etree
from fake_useragent import UserAgent
import time


def req_page(url, page_num=None):
    ua = UserAgent(path='./fake_useragent.json')
    headers = {
        'user-agent': ua.random
    }
    params = {
        'page': page_num
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    return html


def get_page_num(url):
    page = req_page(url)
    page_num = page.xpath("//div[@class='pagenav']//text()")
    return page_num


def list_page(url):
    domain_url = 'https://fmovies.to'
    page_nums = get_page_num(url)
    a_hrefs = []
    data = {}
    for page_num in page_nums:
        if page_num.isdigit():
            print('获取第{}页数据>>>>>>>>>'.format(page_num))
            page = req_page(url, page_num)
            a_hrefs = [domain_url + href for href in page.xpath('//h3/a/@href')]
            title = page.xpath("//h3/a/@title")
            dic = dict(zip(title, a_hrefs))
            data.update(dic)
            time.sleep(2)
    print(data)
    print(len(data))
    return None


# def get_video_links(urls):
#     for url in urls:
#         page_text = req_page(url)
#         page_text.xpath()


def main(url):
    urls = list_page(url)
    # get_video_links(urls)


if __name__ == '__main__':
    url1 = 'https://fmovies.to/tv-series'
    main(url1)
