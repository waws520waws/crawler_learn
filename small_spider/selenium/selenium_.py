'''
- selenium作用：
    - 便捷获取网站中动态加载的数据
    - 便捷实现模拟登陆
- 如何使用：
    - 安装selenium包
    - 下载一个浏览器的驱动程序（需要下载与浏览器版本对应的驱动程序）
        - google：http://chromedriver.storage.googleapis.com/index.html
        - hotfire：https://github.com/mozilla/geckodriver/releases/
        - IE：http://selenium-release.storage.googleapis.com/index.html
- 设置浏览器窗口大小
    - 最大化和最小化浏览器
        - driver.maximize_window()
        - driver.minimize_window()
    - 将浏览器设置一个指定大小
        - driver.set_window_size(100, 50)
- 截图问题
    - 缩放比例的问题。如果你的谷歌浏览器调整成80%缩放就不会有问题，默认打开是100%。3种解决方式：
        - 1.driver.execute_script(document.body.style.zoom=0.8)，执行这样的JS代码
        - 2.浏览器默认100%，将location，size的值，每个值都乘以5/4
        - 3.直接截标签 code_img = driver.find_element_by_xpath('//*[@id="loginImg"]').screenshot('code.png')
'''


from selenium import webdriver
from lxml import etree
import time

## 设置成无可视化界面（亦称无头浏览器，phantomJs亦是）
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % ip)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

## selenium规避被检测识别
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实力化一个浏览器对象
webdri = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options, options=option)

## 1、实现自动搜索‘iPhone’

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