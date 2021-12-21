
from selenium import webdriver
from lxml import etree
import time

## 设置成无可视化界面（亦称无头浏览器，phantomJs亦是）
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % ip)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实力化一个浏览器对象
webdri = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

## 1、实现自动搜索‘iPhone’
## 等待加载的方式见 wait_load_setting.py 文件

webdri.get('https://www.taobao.com/')
# 定位元素
search_input = webdri.find_element_by_id('q')
# 交互
search_input.send_keys('iphone')

btn = webdri.find_element_by_css_selector('.btn-search')
# 点击按钮
btn.click()

# 滚动屏幕（通过js脚本）
webdri.execute_script('window.scrollTo(0,document.body.scrollHeight)')

## 2、然后跳转到百度，获取数据后，再返回到淘宝页面

webdri.get('https://www.baidu.com')

# 获取网页源码数据
page_text = webdri.page_source

page_etree = etree.HTML(page_text)

news = page_etree.xpath('//ul[@class="s-news-rank-content"]')

# 页面后退
webdri.back()
# # 页面前进
# webdri.forward()

time.sleep(5)

## 窗口之间的切换
webdri.switch_to.window(webdri.window_handles[-1])  # 切换到最后一个窗口


webdri.quit()