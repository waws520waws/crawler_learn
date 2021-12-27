'''
本案例解决 汽车之家 里的字体反爬（关键字体经过js生成）
https://car.autohome.com.cn/config/series/59.html#pvareaid=3454437

'''

from selenium import webdriver
import re
import time
import requests


def get_info(html):
    '''
    1、网页中的信息都在 config 和 optopn 两个变量中，
        拿到的信息是残缺的（需要根据js规则得出残缺的信息）
    2、拿到js规则代码
    :param html:
    :return:
    '''

    config = re.search('var config = (.*?)};', html, re.S)
    option = re.search('var option = (.*?)};', html, re.S)

    car_info = ''
    if config and option:
        car_info = car_info + config.group(0) + option.group(0)

    ## 2
    js_code = re.search(r'<script>(.*?)</script>', html, re.S).group(1)
    if js_code:
        with open('jsCode.js', 'w', encoding='utf-8') as f:
            f.write(js_code)

    return car_info


def write_html(js_list, car_info):
    '''
    根据js规则得出残缺的信息
    :param js_list: js规则
    :param car_info: 残缺的信息
    :return:
    '''
    # 运行JS的DOM -- 这部破解是最麻烦的，非常耗时间~参考了互联网上的大神代码
    DOM = ("var rules = '2';"
           "var document = {};"
           "function getRules(){return rules}"
           "document.createElement = function() {"
           "      return {"
           "              sheet: {"
           "                      insertRule: function(rule, i) {"
           "                              if (rules.length == 0) {"
           "                                      rules = rule;"
           "                              } else {"
           "                                      rules = rules + '#' + rule;"
           "                              }"
           "                      }"
           "              }"
           "      }"
           "};"
           "document.querySelectorAll = function() {"
           "      return {};"
           "};"
           "document.head = {};"
           "document.head.appendChild = function() {};"

           "var window = {};"
           "window.decodeURIComponent = decodeURIComponent;")

    # 把JS文件写入到文件中去
    for item in js_list:
        DOM = DOM + item
    html_type = "<html><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /><head></head><body>    <script type='text/javascript'>"
    # 拼接成一个可以运行的网页
    js = html_type + DOM + " document.write(rules)</script></body></html>"
    # 再次运行的时候，请把文件删除，否则无法创建同名文件，或者自行加验证即可
    with open("./demo.html", "w", encoding="utf-8") as f:
        f.write(js)

    # 通过selenium将数据读取出来，进行替换
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96', chrome_options=chrome_options)
    driver.get("file:///Users/jieyang/PycharmProjects/crawler_learn/Python爬虫100例教程/7反爬-64-字体反爬2(汽车之家)/demo.html")
    # 读取body部分
    text = driver.find_element_by_tag_name('body').text
    # print(text)
    driver.quit()
    # 匹配车辆参数中所有的span标签
    cls_list = re.findall("<span class='(.*?)'></span>", car_info)  # 原信息中需要替换的span的类名

    for cls_name in cls_list:
        rex = re.search('\.%s::before { content:"(.*?)" }' % cls_name, text)
        if rex:
            key_info = rex.group(1)  # 得到关键信息
            car_info = car_info.repalce(f"<span class='{cls_name}'></span>", f"<span class='{cls_name}'>{key_info}</span>")

    print(car_info)



def main():
    url = 'https://car.autohome.com.cn/config/series/59.html'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

    res = requests.get(url, headers=headers).text
    car_info = get_info(res)

    with open('jsCode.js', 'r', encoding='utf-8') as f:
        js_list = f.readlines()

    write_html(js_list, car_info)


if __name__ == '__main__':
    main()