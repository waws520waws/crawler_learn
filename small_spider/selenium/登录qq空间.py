from selenium import webdriver
from selenium.webdriver import ActionChains
import time

webdri = webdriver.Chrome(executable_path='./chromedriver.exe')

webdri.get('https://qzone.qq.com/')

webdri.switch_to.frame('login_frame')

switch_login = webdri.find_element_by_id('switcher_plogin')
switch_login.click()

input_id = webdri.find_element_by_id('u')
input_id.send_keys('1410203345')
input_pw = webdri.find_element_by_id('p')
input_pw.send_keys('jie970706')

btn = webdri.find_element_by_id('login_button')
btn.click()

## 这里一定要等一会儿，等待页面加载出来，否则xpath定位不带元素
time.sleep(3)
webdri.switch_to.frame(webdri.find_element_by_xpath('//div[@id="newVcodeIframe"]/iframe'))  # 3

tcaptcha_drag = webdri.find_element_by_id('tcaptcha_drag_thumb')

action = ActionChains(webdri)
action.click_and_hold(tcaptcha_drag)
# 滑动多少像素点此时还不知
action.move_by_offset(200, 0).perform()

action.release()

time.sleep(3)
webdri.quit()

