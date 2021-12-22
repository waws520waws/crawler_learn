'''
此案例为网上找的识别极验证的验证码
并不是100例中的例58
参考：https://buwenbuhuo.blog.csdn.net/article/details/109182895
'''

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from PIL import Image


url = 'https://captcha1.scrape.center/'


def save_img(driver):
    # driver.save_screenshot('./screen1.png')
    time.sleep(2)
    # 获取验证码的定位（方法1：这里选择直接截取标签）
    img = driver.find_element_by_class_name("geetest_canvas_img").screenshot('./img2.png')
    img = driver.find_element_by_class_name("geetest_canvas_img")
    print(img.location, img.size)

    '''方法2（下面代码未考虑浏览器缩放问题，会有问题）
    
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
    '''

    ## 保存完整的验证码图片

    # 将下面的值改为 block，就可显示完整的图片
    driver.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style = 'display: block'")

    img = driver.find_element_by_class_name("geetest_canvas_img").screenshot('./fullImg.png')
    img = driver.find_element_by_class_name("geetest_canvas_img")
    print(img.location, img.size)


def discern_distance():
    '''
    1、滑块宽42px，左高距左边界6px
    2、多抛几个像素，定为55px (因为缺口不会与滑块挨得过近，也防止滑块边界的影响)
    3、对图片中（55，0）右下方的区域的每一个像素点一一对比，找到差别最大的，即为缺口所在位置
    4、经测，发现差值大于30左右的可以既去掉 灰色阴影的干扰块 又能识别出缺口位置
        - 怎么测：可以将像素值不同的全打印出来观察 或者 打印差值
    :return:
    '''
    fullImg = Image.open('fullImg.png')
    img_obj = Image.open('img2.png')

    for x in range(55, img_obj.width):
        for y in range(img_obj.height):
            # getpixel() 获取图像中某一点的像素的RGB颜色值（默认），返回的是坐标点（x，y）处的red，green，blue的数值（三元组）
            p1 = fullImg.getpixel((x, y))
            p2 = img_obj.getpixel((x, y))

            if abs(p1[0]-p2[0]) > 30 and abs(p1[1]-p2[1]) > 30 and abs(p1[2]-p2[2]) > 30:
                distance = x - 6  # 左高距左边界6px
                print('移动距离为：', distance)
                return distance


def get_tracks(distance, rate=0.5, t=0.2, v=0):
    """
    将distance分割成小段的距离
    :param distance: 总距离
    :param rate: 加速减速的临界比例
    :param a1: 加速度
    :param a2: 减速度
    :param t: 单位时间
    :param t: 初始速度
    :return: 小段的距离集合
    """
    tracks = []
    # 加速减速的临界值
    mid = rate * distance
    # 当前位移
    s = 0
    # 循环
    while s < distance:
        # 初始速度
        v0 = v
        if s < mid:
            a = 3
        else:
            a = -2
        # 计算当前t时间段走的距离
        s0 = v0 * t + 0.5 * a * t * t
        # 计算当前速度
        v = v0 + a * t
        # 四舍五入距离，因为像素没有小数
        tracks.append(round(s0))
        # 计算当前距离
        s += s0

    print(tracks)

    return tracks


def slide(driver, distance):
    button = driver.find_element_by_class_name('geetest_slider_button')
    print(button.location)
    while True:

        ActionChains(driver).click_and_hold(button).perform()

        # action.move_by_offset(50, 0).perform()

        # 模拟人的移动轨迹
        ## 这里移动的轨迹还不够随机，可能会被识别出来
        tracks = get_tracks(distance)
        for track in tracks:
            print(track)
            ActionChains(driver).move_by_offset(track, 0).perform()
            newBtn = driver.find_element_by_class_name('geetest_slider_button')
            print(newBtn.location)

        ActionChains(driver).release().perform()

        time.sleep(5)

        # 判断
        if driver.current_url == url:
            print("失败...再来一次...")
            # 单击刷新按钮刷新
            driver.execute_script('document.getElementsByClassName("geetest_refresh_1")[0].click()')
            # 停一下
            time.sleep(2)
            # 截图
            save_img(driver)
            # 识别
            distance = discern_distance()
        else:
            print("成功")
            break


def get_canvas_img(driver):
    driver.find_element_by_class_name("el-button").click()


def main():
    url = 'https://captcha1.scrape.center/'
    # driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96')
    driver = webdriver.Chrome('D:/pyEnvsPackage/chromedriver_win32_92/chromedriver.exe')

    # driver.maximize_window()
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
    distance = discern_distance()
    # 滑动
    slide(driver, distance)

    driver.close()


if __name__ == '__main__':
    main()