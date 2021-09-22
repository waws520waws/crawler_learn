from selenium import webdriver
import time

# 新版本的PIL库更改为pillow
from PIL import Image

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(3)

a_login = driver.find_element_by_xpath('//li[@class="login-hd-account"]/a')
a_login.click()
time.sleep(2)

driver.save_screenshot('./screenImg.png')

## 法1：直接截标签

# imgcode = driver.find_element_by_xpath('//img[@class="imgCode"]').screenshot('./codeImg.png')

## 法2：

driver.execute_script('document.body.style.zoom=0.8')

# imgcode = driver.find_element_by_xpath('//img[@class="imgCode"]')
#
# # 图片起始位置
# location = imgcode.location
#
# size = imgcode.size
#
# shot_location = (location['x'], location['y'], location['x']+size['width'], location['y']+size['height'])
#
# screenImg = Image.open('./screenImg.png')
# shot_code = screenImg.crop(shot_location)
# shot_code.save('./codeImg.png')



