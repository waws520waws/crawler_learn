### 1、简介
- selenium作用：
    - 便捷获取网站中动态加载的数据
    - 便捷实现模拟登陆
    - 适合每天爬取数据量要求不高的爬虫工作
- 优点
    - Selenium支持跨不同 浏览器，平台 和 编程语言 的自动化
    - 完善、稳定
- 缺点
    - 速度太慢、对版本配置要求严苛，最麻烦是经常要更新对应的驱动。
    - 还有些网页是可以检测到是否是使用了selenium 。
    - 并且selenium 所谓的保护机制不允许跨域 cookies 保存以及登录的时候必须先打开网页然后后加载 cookies 再刷新的方式很不友好
    
### 2、使用：
#### 2.1 安装
- 安装selenium包
- 下载一个浏览器的驱动程序（需要下载与浏览器版本对应的驱动程序）
    - google：http://chromedriver.storage.googleapis.com/index.html
    - hotfire：https://github.com/mozilla/geckodriver/releases/
    - IE：http://selenium-release.storage.googleapis.com/index.html
#### 2.2 使用
- 1）设置浏览器窗口大小
    - 最大化和最小化浏览器
        - `driver.maximize_window()`
        - `driver.minimize_window()`
    - 将浏览器设置一个指定大小
        - `driver.set_window_size(100, 50)`
- 2）截图问题
    - 缩放比例的问题。如果你的谷歌浏览器调整成80%缩放就不会有问题，默认打开是100%。3种解决方式：
        - 1.`driver.execute_script(document.body.style.zoom=0.8)`，执行这样的JS代码
        - 2.浏览器默认100%，将location，size的值，每个值都乘以5/4
        - 3.直接截标签 `code_img = driver.find_element_by_xpath('//*[@id="loginImg"]').screenshot('code.png')`
    
### 3、如何更改selenium标识，防止被检测出来
- 使用selenium时，window.navigator.webdriver 的值为 true，我们要将其改为false
- 访问这个网站可以测试是否设置成功：https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html
  
- 方法1：执行以下脚本
```python
driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
```
- 问题：有时候设置了webdriver的值，但还是访问不了网站，此时可以换个浏览器试试


- 方法2：使用 mitmproxy 进行代理（拦截请求并设置请求参数）
    - 步骤1、带脚本启动mitm代理 `mitmdump -s selenium_proxy.py`
    - 步骤2、在selenium中设置代理（上一步启动mitm后会显示监听的端口号，地址默认为127.0.0.1）
    - 步骤3、运行seleniumScript.py
    - 【实例：100例57】
```python
# selenium_proxy.py
from mitmproxy import ctx

injected_javascript = '''
// overwrite the `languages` property to use a custom getter
Object.defineProperty(navigator, "languages", {
  get: function() {
    return ["zh-CN","zh","zh-TW","en-US","en"];
  }
});
// Overwrite the `plugins` property to use a custom getter.
Object.defineProperty(navigator, 'plugins', {
  get: () => [1, 2, 3, 4, 5],
});
// Pass the Webdriver test
Object.defineProperty(navigator, 'webdriver', {
  get: () => false,
});
// Pass the Chrome Test.
// We can mock this in as much depth as we need for the test.
window.navigator.chrome = {
  runtime: {},
  // etc.
};
// Pass the Permissions Test.
const originalQuery = window.navigator.permissions.query;
window.navigator.permissions.query = (parameters) => (
  parameters.name === 'notifications' ?
    Promise.resolve({ state: Notification.permission }) :
    originalQuery(parameters)
);
'''


def response(flow):
    # Only process 200 responses of HTML content.
    if not flow.response.status_code == 200:
        return

    # Inject a script tag containing the JavaScript.
    html = flow.response.text
    html = html.replace('<head>', '<head><script>%s</script>' % injected_javascript)
    flow.response.text = str(html)
    ctx.log.info('>>>> js代码插入成功 <<<<')

    # 只要url链接以target开头，则将网页内容替换为目前网址
    # target = 'https://target-url.com'
    # if flow.url.startswith(target):
    #     flow.response.text = flow.url
```

```python
# seleniumScript.py
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://127.0.0.1:8080")
driver = webdriver.Chrome('/Users/jieyang/Downloads/chromedriver96', options=options)
driver.get('https://www.baidu.com')
# 。。。。其他操作
```

- 存在的问题（跳转到新的标签页时selenium被反爬识别）
    - 有的网站中的超链接是在新的标签页中打开，如果网站新的页面也加入了验证（一般都会加的）那么我们还是没有办法验证通过，解决办法其实也非常简单，
      我们通过selenium把页面中所有的超链接都增加一个 target属性，并且把值设置为 _self，表示在当前页中打开链接。
        ```python
        driver.implicitly_wait(10)
        driver.get("https://passport.csdn.net/login?code=public")
        
        js =  "let a_list = document.getElementsByTagName('a');[...a_list].map(a => {a.setAttribute('target', '_self')})"
        driver.execute_script(js)  # 执行JavaScript代码
        ```
      
    - 在当前标签页中打开指定链接
        ```python
        # 跳转页面
        time.sleep(2)
        new_window = 'window.open("{}", "_self")'.format("https://i.csdn.net/#/uc/profile")  
        driver.execute_script(new_window)
        driver.implicitly_wait(10)
        ```
      
- 方法3
    - 一个webdirver的驱动模块，但是并不是selenium，而是 undetected_chromedriver；
      这个模块可以完美的模拟chrome浏览器，并且不用设置js默认值，也就是无需自己再添加瞒天过海的设置
      - 【参考】https://blog.csdn.net/m0_60570576/article/details/121429251