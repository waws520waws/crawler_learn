from appium import webdriver
from time import sleep
from multiprocessing import Process


class TouTiao(object):

    def __init__(self, driver):
        self.driver = driver

    def handle_appium(self, device, port):
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': device,
            'udid': device,
            'appPackage': 'com.ss.android.article.lite',
            'appActivity': '.activity.SplashActivity'
        }
        self.driver = webdriver.Remote(f'http://localhost:{port}/wd/hub', self.desired_caps)
        # 当资源未加载出时,最大等待时间15S（对于所有操作），资源加载出来才执行下一步操作
        self.driver.implicitly_wait(15)
        self.pass_windows()

    def pass_windows(self):
        # 根据app提示一步一步操作
        self.driver.find_element_by_id('com.ss.android.article.lite:id/vj').click()
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_deny_button').click()
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_deny_button').click()
        self.driver.find_element_by_id('com.ss.android.article.lite:id/r9').click()
        # 上滑一次
        self.driver.swipe(373, 1029, 373, 387)
        # 下滑800次（为什么是800次，视频中会讲原因）
        for i in range(800):
            self.driver.swipe(373, 178, 373, 1029)
            sleep(4)

    # 关闭App
    def close_app(self):
        self.driver.close_app()

    def run(self):
        devices = ['127.0.0.1:62001', '127.0.0.1:62025']
        p_list = []
        for device in range(len(devices)):
            '''
            一般Server Port 以及 Bootstrap Port 挨着编号，
            如：如appium服务端第一个设置为 4723（Server Port） 以及 4724（Bootstrap Port）,
                第2个设置为 4725（Server Port） 以及 4726（Bootstrap Port）
            则每一个Server Port相差2
            '''
            server_port = 4723 + 2 * device
            p = Process(target=self.handle_appium, args=(devices[device], server_port))
            p.start()
            p_list.append(p)

        for p in p_list:
            p.join()

        self.close_app()


if __name__ == '__main__':

    while True:

        try:
            driver = ''
            toutiao = TouTiao(driver)
            toutiao.run()
        except:
            continue
