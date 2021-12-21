'''
此案例为网上找的识别极验证的验证码
并不是100例中的例58
参考：https://buwenbuhuo.blog.csdn.net/article/details/109182895
'''

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image


def save_img(driver):
    driver.save_screenshot('./screen1.png')
    time.sleep(2)
    # 获取验证码的定位
    img = driver.find_element_by_class_name("geetest_canvas_img")
    # print(img1.location,img1.size)#{'x': 590, 'y': 239} {'height': 160, 'width': 260}
    # 坐标（左上角，右下角）
    rectangle = (
        img.location['x'], img.location['y'], img.location['x']+img.size['width'], img.location['y']+img.size['height'])
    print(rectangle)
    # 打开图片
    img_obj = Image.open('./screen1.png')
    # 截图
    img_new = img_obj.crop(rectangle)
    # 保存
    img_new.save('./img1.png')

    driver.quit()


def get_canvas_img(driver):
    driver.find_element_by_class_name("el-button").click()

def main():
    url = 'https://captcha1.scrape.center/'
    driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96')
    driver.get(url)

    driver.find_elements_by_class_name('el-input__inner')[0].send_keys('qqqq')
    driver.find_elements_by_class_name('el-input__inner')[1].send_keys('11111')
    driver.find_element_by_class_name("el-button").click()

    # 此网站可能需要多次点击才会弹出验证码框
    while True:
        try:
            time.sleep(5)
            driver.find_element_by_class_name('geetest_canvas_img')
            break
        except Exception as e:
            print('重新点击按钮。。。')
            get_canvas_img(driver)


    time.sleep(5)

    # 保存图片
    save_img(driver)
    # 识别位移
    # discern_distance()
    # 滑动
    # slide(driver)

    # driver.close()



if __name__ == '__main__':
    main()