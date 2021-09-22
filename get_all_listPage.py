import re
import time
import requests
from lxml import etree


def view_url(links):
    for link in links:
        print(link)
    print(len(links), '\n')
    return None


def get_html(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36'
    }
    req = requests.get(url, headers=header)
    html = req.text
    html = etree.HTML(html)
    return html


def get_detail_link(list_page_links):
    labels = ['h2', 'h3', 'h4']
    used_labels = []
    detail_links = []
    for link in list_page_links:
        print('using link is: ', link)
        html = get_html(link)
        for label in labels:
            path = "//{}/a/@href".format(label)
            detail_link = html.xpath(path)
            # 有数据，则保存
            if detail_link:
                used_labels.append(label)
                detail_links.append(detail_link)
        break
    print('detail links: ')
    view_url(used_labels)
    view_url(detail_links[0])
    return None


def detail_or_list_page(links):

    detail_page = []
    list_page = []
    for link in links:
        is_detail = False
        for otherlink in links:
            if link == otherlink:
                continue
            elif link.startswith(otherlink):
                detail_page.append(link)
                is_detail = True
                continue
        if not is_detail:
            list_page.append(link)
    print('detail page: ')
    view_url(detail_page)
    print('list page: ')
    view_url(list_page)

    return list_page


def get_menu_link(url):

    html = get_html(url)

    # links = html.xpath("(//ul)[position()<3]//a[re:match(@href, 'https://www\.thehealthsite\.com/.*')]/@href",
    #                    namespaces={"re": "http://exslt.org/regular-expressions"})

    # 完整link
    path = "(//ul)[position()<3]//a[starts-with(@href, '{}')]/@href".format(url)
    links = html.xpath(path)

    # /xxx/xx/ 形式的link
    if not links:
        path = "(//ul)[position()<3]//a[starts-with(@href, '/')]/@href"
        links = html.xpath(path)
        links = [url + i for i in links]

    print('all of menu links: ')
    view_url(links)

    list_page_links = detail_or_list_page(links)

    return list_page_links


def main():
    url = 'https://www.thehealthsite.com'
    url1 = 'https://screenrant.com'
    list_page_links = get_menu_link(url1)
    get_detail_link(list_page_links)


if __name__ == '__main__':
    main()
