import random
import time

from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

## 更改selenium的标识，防止被检测出来
## 使用selenium时，window.navigator.webdriver 的值为 true，我们要将其改为false

### 方法1：执行以下脚本
# driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96')
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => false
#     })
#   """
# })

### 方法2：使用 mitmproxy 进行代理
'''
步骤：
    1、带脚本启动mitm代理 `mitmdump -s selenium_proxy.py`
    2、在selenium中设置代理（上一步启动mitm后会显示监听的端口号，地址默认为127.0.0.1）
    3、运行selenium
'''

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=127.0.0.1:8080")
driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96', options=options)
driver.get('https://promotion.aliyun.com/ntms/act/captchaIntroAndDemo.html')


def move_to_gap(tracks):
    move_span = driver.find_element_by_id('nc_1_n1z')
    action = ActionChains(driver)
    action.click_and_hold(move_span).perform()
    for x in tracks:  # 模拟人的拖动轨迹
        print(x)
        action.move_by_offset(xoffset=x, yoffset=random.randint(1, 3)).perform()
    time.sleep(1)
    action.release().perform()  # 释放左键


# 这个地方可以借鉴网上的方案即可
def get_track(distance):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+(1/2)at²
    ③v²-v0²=2as

    :param distance: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    '''
    # 初速度
    v = 0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t = 0.1
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达mid值开始减速
    mid = distance * 4 / 5

    distance += 10  # 先滑过一点，最后再反着滑动回来

    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = 2  # 加速运动
        else:
            a = -3  # 减速运动

        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t

    # 反着滑动到大概准确位置
    for i in range(3):
        tracks.append(-2)
    for i in range(4):
        tracks.append(-1)
    return tracks


move_to_gap(get_track(295))
