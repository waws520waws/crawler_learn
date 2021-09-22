from selenium import webdriver
driver = webdriver.Chrome(executable_path='./selenium/chromedriver')

## 1、强制等待
import time
time.sleep(3)

## 2、隐式等待
# 设置一个等待时间，后面的操作会等待，如果在这个等待时间内，加载完成，则执行下一步；否则一直等待直到设置的时间，然后再执行下一步
driver.implicitly_wait(30)


## 3、显示等待
'''
主要有4个参数：
driver：浏览器驱动
timeout：等待时间
poll_frequency：检测的间隔时间，默认0.5s
ignored_exceptions：超时后的异常信息，默认抛出NoSuchElementException
'''
from selenium.webdriver.support.wait import WebDriverWait
text = WebDriverWait(driver, 30, 0.2).until(lambda x: x.find_element_by_css_selector(".tt")).text

# 或者
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
wait(driver, 30, 0.2).until(EC.presence_of_element_located((By.XPATH, "//div[@id='player']//iframe")))