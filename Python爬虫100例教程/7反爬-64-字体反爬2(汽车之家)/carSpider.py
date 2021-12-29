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
    1、网页中的信息都在 keyLink、config 和 option 三个变量中，
        拿到的信息是残缺的（需要根据js规则得出残缺的信息）
    2、拿到js规则代码 (三个规则，分别对应三个变量)
    :param html:
    :return:
    '''

    keyLink = re.search('var keyLink = (.*?)];', html, re.S)
    config = re.search('var config = (.*?)};', html, re.S)
    option = re.search('var option = (.*?)};', html, re.S)

    car_info = ''
    if keyLink and config and option:
        car_info = car_info + keyLink.group(0) + config.group(0) + option.group(0)
    print(car_info)
    ## 2
    js_code_list = re.findall(r'<script>(.*?document\);).*?</script>', html, re.S)

    if len(js_code_list):
        return car_info, js_code_list
    else:
        print('未匹配到 js 代码，退出！')
        quit()

def write_html(js_list, car_info):
    '''
    根据js规则得出残缺的信息。
    残缺的信息是执行js代码后生成的，两种方式生成：
        - 1、构造一个html文件，里面写入js代码，使用selenium访问这个文件时，执行这些js代码，将其生成为网页元素，再读取（本案例使用此方法）
        - 2、关键信息在js代码中的 $sheet$ 变量中，使用 execjs 执行js代码，在读取这个变量 （未尝试）

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
    # time.sleep(100)
    driver.quit()
    # 匹配车辆参数中所有的span标签
    cls_list = re.findall("<span class='(.*?)'></span>", car_info)  # 原信息中需要替换的span标签的类名

    for cls_name in cls_list:
        rex = re.search('\.%s::before { content:"(.*?)" }' % cls_name, text)  # 匹配span的类名所对应的关键信息
        if rex:
            key_info = rex.group(1)  # 得到关键信息
            car_info = car_info.replace(f"<span class='{cls_name}'></span>", f"<span class='{cls_name}'>{key_info}</span>")

    print(car_info)



def main():
    url = 'https://car.autohome.com.cn/config/series/59.html'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

    res = requests.get(url, headers=headers).text
    car_info, js_list = get_info(res)

    write_html(js_list, car_info)


if __name__ == '__main__':
    main()