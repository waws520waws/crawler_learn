### app自动化测试工具 Appium
- 简介：Appium 是一种开源、跨平台的测试自动化工具，适用于原生、混合和移动 Web 和桌面应用程序。
  支持模拟器 (iOS)、模拟器 (Android) 和真实设备 (iOS、Android、Windows、Mac)。  
  它有点类似Selenium，可以自动操作APP实现一系列的操作。
- 特点：
    - 可以使用python（任何WebDriver兼容的语言）对Appium编写脚本，实现对App的抓取
    - 解放人力
    - 操作精准快速,并支持同时操作多台手机
    - 部分数据可以直接通过Appium拿到
- appium爬虫的思路
    - 让Appium代替我滑动手机，甚至这一步可以跳过，我直接手动滑动，一边刷抖音的同时，让手机自己生成加密后的参数去请求服务器，
      让抓包工具去执行Python脚本，劫持服务器返回的视频资源就行了。虽然速度没有request和Scrapy相比，但是还好Appium支持同时控制多台手机。
- 安装：
    - 【参考】https://zhuanlan.zhihu.com/p/49193525
    - 【appium下载地址】https://github.com/appium/appium-desktop/releases
    - 【注意事项】
        - 模拟器的adb 与 Android SDK的adb版本要一致
            - 【参考】https://blog.csdn.net/hihell/article/details/86233963
        - Inspector 与 appium分开了，需要手动下载Inspector客户端
            - 【Inspector下载地址】https://github.com/appium/appium-inspector
- 适用场景
    - 【参考】https://www.zhihu.com/people/Wubba-lubba-dub-dub/posts
    - 以下情况，可以考虑使用Appium:
        - 你要爬的数据不是太多，你又懒得写代码
        - 参数加密太难搞定或者网站反爬太严格
        - 有些数据App特有
        - 每天定点注册，有短信加滑动验证码
        - 就是自己私底下想搞些节省人力的小脚本
    - 以下情况，请不要优先使用Appium：
        - 老大急着要数据
        - 爬取数据量巨大，除非你有大量闲置电脑或者手机
        - 必须追求稳定，因为模拟器和手机偶尔抽风也很正常。
        - 硬件性能不高，如果用安卓模拟器，必须要有显卡，否则模拟器不让你安装，即使安装上也卡成PPT，
          不过我后边会介绍如何将模拟器部署Docker,因为是无界面的，比较轻量级，对显卡也无硬性要求。
  
- 使用
    - 【参考】https://zhuanlan.zhihu.com/p/49428952
    - 【参考】https://blog.csdn.net/hihell/article/details/86233963
    - 1、使用cmd命令连接模拟器
        - `adb.exe connect 127.0.0.1:62001` adb连接夜神模拟器的端口号为62001，其他模拟器的端口号见参考链接
        - 检查设备是否连接 `adb devices [-l]`
    - 2、启动appium服务
        - Appium Server GUI 桌面快捷图标
    - 3、启动 Appium Inspector 桌面快捷图标
    - 4、查看app的包名与进程名
        - 0）在终端输入 ：`adb devices`, 检查设备是否还是连接状态
        - 1）模拟器打开app
        - 2）在终端输入： `adb shell`，进入adb shell 终端
        - 3）输入 `dumpsys activity | grep mFocusedActivity`, 可查看app的包名与进程名
    - 5、Appium Inspector中输入手机配置信息
        ```text
        {
          "platformName": "Android",   # 声明是ios还是Android系统
          "platformVersion":"4.4.2",   # Android内核版本号，可以在夜神模拟器设置中查看   
          "deviceName": "OPPO R11",  # 这个地方我们可以写 127.0.0.1:62001 (一般写 `adb devices` 后显示的名称)
          "appPackage": "com.taobao.taobao",  #  apk的包名 
          "appActivity": "com.taobao.tao.welcome.Welcome"  # apk的launcherActivity
        }
        ```
        其他的参数：参考https://blog.csdn.net/xyz846/article/details/50750701
    - 【遇到的问题】
        - 1）Appium Inspector 点击 start session 后报错
            - 报错 `Failed to create session. The requested resource could not be found, or a request was received using an HTTP method that is not supported by the mapped resource`
            - 解决方法：Remote Path处填写 `/wd/hub`
    
- python脚本的使用
    - 【参考】https://zhuanlan.zhihu.com/p/50515738
    - 安装： `pip install Appium-Python-Client`
    - 例子：见 appium_douyin.py
    - 运行脚本：直接在pycharm中右键点击运行（得先连接设备，并打开appium服务端，方法见上一步）
    - 常用方法
        ```python
        # 得到设备屏幕分辨率宽高
        self.driver.get_window_size()
        # 截图
        self.driver.save_screenshot()
        # 滑动事件,参数填写起始点横纵坐标,结束点横纵坐标,相当于按住起始点,移动到终点,松开
        self.driver.swipe(start_x, start_y, end_x, end_y)
        # 点击指定坐标位置
        self.driver.tap()
      
        # 通过id查找多个元素
        self.driver.find_elements_by_id()
        # 通过xpath查找多个元素
        self.driver.find_elements_by_xpath()
        # 通过name查找多个元素
        self.driver.find_elements_by_name()
      
        # 通过id查找元素,并点击
        self.driver.find_elements_by_id().click()
      
        # 通过id查找元素,并输入内容
        self.driver.find_elements_by_id().send_keys()
        ```

### Android 加密解密的几种方式
- 经常使用的加密算法: Base64、DES、3DES、RC4、AES，RSA等;
- 对称加密：des，3des，aes
- 非对称加密：rsa
- 不可逆加密：md5
- 加密模式:ECB、CBC、CFB、OFB等;
- 填充模式:NoPadding、PKCS1Padding、PKCS5Padding、PKCS7Padding

### adb工具
- 【参考】https://blog.csdn.net/qq_36424455/article/details/105467734
- 什么是adb?
    - 简单来说,ADB是来调试Android开发工具,ADB（Android Debug Bridge）是Android SDK中的一个工具, 使用ADB可以直接操作管理Android模拟器或者真实的Andriod设备。
-  ADB主要功能有:
    - 1）在Android设备上运行度Shell(命令行)
    - 2）管理模拟器或设备的端口映射
    - 3）在计算机和知设备之间上传/下载文件