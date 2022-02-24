from appium import webdriver
from time import sleep


class TouTiao(object):

    def __init__(self):
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': 'SM_G973N',
            'appPackage': 'com.ss.android.article.lite',
            'appActivity': '.activity.SplashActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        # 当资源未加载出时,最大等待时间15S（对于所有操作），资源加载出来才执行下一步操作
        self.driver.implicitly_wait(15)

    def pass_windows(self):
        # 根据app提示一步一步操作
        self.driver.find_element_by_id('com.ss.android.article.lite:id/vj').click()
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_deny_button').click()
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_deny_button').click()
        self.driver.find_element_by_id('com.ss.android.article.lite:id/r9').click()
        self.driver.find
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
        self.pass_windows()
        self.close_app()


if __name__ == '__main__':

    while True:

        try:
            toutiao = TouTiao()
            toutiao.run()
        except:
            continue
