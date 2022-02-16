### 手机App爬虫归类
- 1、 50%的app，通过抓包软件就可以分析出抓取参数并抓取到信息。
- 2、 30%的app，可能需要适当的反编译，分析出加密算法并抓取到信息。
- 3、 10%的app，可能加固，需要脱壳，然后反编译，分析出加密算法并抓取到信息
- 4、 10%的app，通过各式各样的签名，证书，设备绑定等方法，隐藏加密算法。

### 抓包
- 抓包是爬虫里面经常用到的一个词，完整的应该叫做抓取 数据请求响应包

## 一、抓包工具
- Fiddler与Charles 功能大同小异，基本上都是抓包、断点调试、请求替换、构造请求、代理功能
- mitmproxy跟Fiddler和Charles最大的不同就是，mitmproxy可以进行二次开发

- 【**注意**】如果是没有无线网卡的 台式机 那似乎只能使用 模拟器 进行网络代理配置

### 1、Fiddler
- Fiddler 运行在Windows平台
- Fiddler 是一款开源免费抓包工具
- 功能大同小异，基本上都是抓包、断点调试、请求替换、构造请求、代理功能
#### 2.1、安装
- 【官网】https://www.telerik.com/fiddler
  - 下载 `Fiddler Classic` 版本
#### 2.2、使用
- 【参考】https://blog.csdn.net/weixin_43664254/article/details/94601280
- 【注意】
  - fiddler默认是抓http请求的，对于pc上的https请求，会提示网页不安全，这时候需要在浏览器上安装证书；
  - 有些设置需要fiddler重启才能生效
  - 如果APP上是https请求，这时候手机需要下载证书（也可以pc上下载证书后传给手机）
  
- 一些功能
  - 接口测试（Composer）
    - 可以模拟发送请求（具体方法参考链接）
  - 打断点
  - 会话（session）保存
    - 作用：下次直接将保存的会话导入到fiddler，不需要再重新请求
  - 自定义会话框
    - 作用：fiddler左边区域添加或者隐藏列
        
### 2、Charles
- Charles 是基于Java实现的，基本上可以运行在所有主流的桌面系统
- Charles 是一款收费的抓包工具，但是支持破解
#### 2.1、安装
- 按照网上的方法就行
- 若手机上无法下载证书，可在电脑浏览器访问下载地址 chl.pro/ssl , 然后将证书传给手机，再安装,  
  手机若提示 '无法安装CA证书' ，可到手机 '设置' --> '安全与隐私' 中找到 '从存储中安装'，即可安装CA,  
  安装好后 charles 上会弹框，然后选择 'allow'
#### 2.2、使用
- 1）请求响应拦截
  - `Proxy` -> `macOS Proxy`  勾选则拦截电脑上的包，取消则不拦截
- 2）断点的使用
  - 作用：拦截请求或者响应包并暂停，此时可以修改请求或者返回的参数
  - 这个功能还是比较实用的，这样就可以省掉一些服务需要的配合，自己可以通过修改数据来模拟不同的情况
  
- 3）重定向（`Map Remote`）
- 4）加载本地数据（`Map Local`）
  - 加载本地的模拟数据来开发测试
  
#### 2.3、出现的问题
- url下出现 <unknown>, 查看unknown的notes里面出现：SSL Proxying not enabled for this host:enable in Proxy Setting,SSL locations
  - 解决方法：`proxy` -> `SSL Proxying Settings` 下设置需要代理的域名和端口号，`*:*` 为代理所有
  

### 3、mitmproxy
- 简介： mitmproxy 就是用于MITM的proxy, MITM即中间人攻击。说白了就是服务器和客户机中间通讯多增加了一层，会适时的查、记录其截获的数据，或篡改数据。
  跟Fiddler和Charles最大的不同就是，mitmproxy可以进行二次开发，尤其可以对接python。  
  **【举例来说，利用 fiddler 可以过滤出浏览器对某个特定 url 的请求，并查看、分析其数据，但实现不了高度定制化的需求，
  类似于：“截获对浏览器对该 url 的请求，将返回内容置空，并将真实的返回内容存到某个数据库，出现异常时发出邮件通知”，
  而对于 mitmproxy，这样的需求可以通过载入自定义 python 脚本轻松实现】**
  
- 由于 mitmproxy 工作在 HTTP 层，而当前 HTTPS 的普及让客户端拥有了检测并规避中间人攻击的能力，
  所以要让 mitmproxy 能够正常工作，必须要让客户端（APP 或浏览器）主动信任 mitmproxy 的 SSL 证书，或忽略证书异常，
  这也就意味着 APP 或浏览器是属于开发者本人的
  
- 实际意义：据我所知目前比较广泛的应用是做仿真爬虫，即利用手机模拟器、无头浏览器来爬取 APP 或网站的数据，
  mitmpproxy 作为代理可以拦截、存储爬虫获取到的数据，或修改数据调整爬虫的行为
  
#### 3.1 安装
- 1）`pip install mitmproxy` 
  - 完成后，系统将拥有 mitmproxy、mitmdump、mitmweb 三个命令
- 2）证书安装
  - 【官方文档】https://docs.mitmproxy.org/stable/overview-getting-started/
  - 【win10】: https://blog.csdn.net/hihell/article/details/86603528
  - 监听谁，谁就需要证书，手机的证书安装参考Charles的方法
- 3）网络代理设置
  - 启动 mitmproxy 后会看到默认端口
  - 电脑代理需要设置成上面看到的ip、port
  - 手机上代理只需设置成电脑的ip（端口默认为8080，可填也可不填）
  
#### 3.2 使用
- 在python环境下启动 mitmproxy，用 `mitmproxy`、`mitmdump`、`mitmweb` 这三个命令中的任意一个即可，这三个命令功能一致，且都可以加载自定义脚本，唯一的区别是交互界面的不同
  - `mitmproxy`    
    mitmproxy 命令启动后，会提供一个命令行界面，用户可以实时看到发生的请求，并通过命令过滤请求，查看请求数据。
    mitmproxy 命令不支持在 windows 系统中运行
    
  - `mitmweb`  
    mitmweb 命令启动后，会提供一个 web 界面，用户可以实时看到发生的请求，并通过 GUI 交互来过滤请求，查看请求数据。
    
  - `mitmdump`  
    mitmdump 命令启动后——你应该猜到了，没有界面，程序默默运行，所以 mitmdump 无法提供过滤请求、查看数据的功能，只能结合自定义脚本，默默工作

- `mitmdump -p 8889` 指定端口启动
    
- 执行python脚本
  - 1）进入到python环境下的某个目录下（带python脚本）
  - 2）带脚本的方式启动 mitmproxy：`mitmdump -s script.py` (如100例中的例子48)
  - 也可以保存数据：`mitmdump -w crawl.txt`
  - 可访问 http://httpbin.org/get 看请求头是否设置成功
- python脚本相关方法
  - 1）mitmdump提供了专门的日志输出功能，可以设定不同级别以不同颜色输出结果。 ctx模块有log功能，调用不同的输出方法就可以输出不同颜色的结果，以方便我们做调试。
```python
from mitmproxy import ctx
def response(flow):
    info = ctx.log.info
    ctx.log.warn(str(flow.request.query))
    ctx.log.error(str(flow.request.headers))

```
  
## 二、app自动化测试工具 Appium
- 简介：Appium 是一种开源、跨平台的测试自动化工具，适用于原生、混合和移动 Web 和桌面应用程序。
  支持模拟器 (iOS)、模拟器 (Android) 和真实设备 (iOS、Android、Windows、Mac)。  
  它有点类似Selenium，可以自动操作APP实现一系列的操作。
  

## 三、APP逆向

### 3.1 绕过证书验证类
- 简介：打开 fiddler 先来抓个包，fiddler 开启之后 app提示连接不到服务器，发现这个 app 做了证书验证
- 解决这种问题一般都是安装 xposed 框架，里面有一个 JustTrustme 模块，它的原理就是hook，直接绕过证书验证类

### 3.2 反编译与混淆技术
- 1、反编译
    - 【参考】https://blog.csdn.net/guolin_blog/article/details/49738023
    - 简介：Android程序打完包之后得到的是一个APK文件，这个文件是可以直接安装到任何Android手机上的，我们反编译其实也就是对这个APK文件进行反编译。
      Android的反编译主要又分为两个部分，一个是对代码的反编译，一个是对资源的反编译。
    - 作用：为了获取app源码（如：获取加密规则代码）
    - 有些APP进行了加固，需要用到脱壳技术，然后再反编译
    
    - 反编译代码：
        - 作用：将APK文件中的代码转换成可读的java代码
        - 可以先将APK文件的后缀改为ZIP，再解压
        - 将APK文件中的代码反编译出来，需要用到两款工具：
            - dex2jar: 这个工具用于将dex文件转换成jar文件
                - dex文件是存放所有java代码的地方
            - jd-gui: 这个工具用于查看源码（此工具将jar文件转换成java代码）
        - 根据请求或响应的参数去源码中搜索需要的东西（如：加密方式）
            - 【**阅读代码技巧**】
                - 需要注意的是，反编译的代码非常混乱，错误很多，并且apk经过混淆，变量名都消失了，这时一定要有有耐心，仔细研究代码。
                - 根据前面请求、响应参数去搜索，或者请求的 url 地址去搜索，而且经验很重要。
                - 如果不知道生成的方式，就用 java运行一波，将这两个参数打印出来
                - 一个技巧：可以使用 xposed 写一个 hook代码 把参数打印出来；或者 使用 frida 来写一段 hook 代码
                    - 【参考】https://www.cnblogs.com/yhoil/articles/14705792.html
                - 一般先从最大的文件开始依次搜索关键字
        
    - 反编译资源
        - 作用：还原APK文件中的9-patch图片、布局、字符串等等一系列的资源
        - 将APK文件中的资源反编译出来，又要用到另外一个工具
            - apktool：这个工具用于最大幅度地还原APK文件中的资源
                - 我们需要的就是 apktool.bat 和 apktool.jar 这两个文件
    - 重新打包
        - 将反编译后的文件重新打包成APK
        - 1）apktool工具将程序文件打包成APK
        - 2）进行签名
            - 作用：若APK没有进行过签名，APK不能安装
            - 没有办法拿到它原来的签名文件，只能拿自己的签名文件来对这个APK文件重新进行签名，但同时也表明我们重新打包出来的软件就是个十足的盗版软件；
              使用Android Studio或者Eclipse都可以非常简单地生成一个签名文件。
            - 签名命令： 
              - cd到jdk的bin目录下，执行：
              - `jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore 签名文件名 -storepass 签名密码 待签名的APK文件名 签名的别名`
        - 3）对齐操作
            - 作用：使得我们的程序在Android系统中运行得更快
            - 使用的是zipalign工具，该工具存放于<Android SDK>/build-tools/<version>目录下，执行：
                - `zipalign 4 New_Demo.apk New_Demo_aligned.apk`
    
- 2、混淆技术
    - 【参考】https://blog.csdn.net/guolin_blog/article/details/50451259
    - 简介：对代码进行混淆，将代码中的类、方法、变量等信息进行重命名，把它们改成一些毫无意义的名字
        - 在Android Studio当中混淆APK实在是太简单了，借助SDK中自带的Proguard工具，只需要修改 build.gradle 中的一行配置即可；
        build.gradle 中 minifyEnabled 的值是false，这里我们只需要把值改成true，打出来的APK包就会是混淆过的了。
            ```text
            release {
                minifyEnabled true
                proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            }        
            ```
        - 根据作者亲身测试得出结论，凡是需要在AndroidManifest.xml中去注册的所有类的类名以及从父类重写的方法名都自动不会被混淆
    - 如何破解混淆
        - 混淆是根据混淆规则来的，那么混淆规则是在哪里定义的呢？
          - 在 build.gradle 的release闭包下配置的 proguard-android.txt 文件中，这个文件存放于 <Android SDK>/tools/proguard 目录下
        - 直接在proguard-android.txt中修改会对我们本机上所有项目的混淆规则都生效，那么有没有什么办法只针对当前项目的混淆规则做修改呢？
          当然是有办法的了，你会发现任何一个Android Studio项目在app模块目录下都有一个proguard-rules.pro文件，这个文件就是用于让我们编写只适用于当前项目的混淆规则的
        - 修改其中的混淆规则
        - 然后反编译
    
### 3.3 APP脱壳
- 加壳（加固）的原理
    - 壳dex 读取 源dex文件，加密后，写进一个新的dex文件
    - 给dex文件加层壳，反编译后的代码就是加壳的代码，看不到原dex代码，在一定程度上来说，还是可以起到防破解的，也可以防止二次打包
- 常用的APP加固壳
    - 360、腾讯乐固、百度、网易、阿里、爱加密、梆梆、娜迦、顶象等
- 查壳工具：
    - ApkScan-PKID
    - 检查一下 app 是否加固，打开 ApkScan-PKID ，把 app 拖入
    - 脱壳原理：在 壳APK 解密 源APK 后，源APK被加载前，拦截（hook技术）这个过程中的系统函数，把内存中的Dex 给dump出来
- 脱壳工具
    - 1）使用 Frida 与 frida-dexdump 对apk 进行 脱壳
        - frida（可以hook住java层、Native层）
        - pc上安装Frida客户端（python环境下安装 Frida），手机（用模拟器吧）中安装Frida服务端
            - `pip3 install frida-tools`
            - 手机端 server 的版本号需要 与 电脑端的一致
            - Frida简介：Frida是个轻量级别的 hook 框架
            - hook技术：
                - 改变程序执行流程的一种技术 在函数被调用前，通过HOOK技术，先得到该函数的控制权，实现该函数的逻辑改写；
                - Hook可以在在Java层、Native层（.so库）；
                - 在代码层 寻找要Hook的地方 进行Hook 改下代码逻辑
        - 安装 frida-dexdump
            - `pip3 install frida-dexdump`
    - 2）基于 xposed 脱壳工具：
        - 【参考】https://blog.csdn.net/qq409732112/article/details/109382336
        - xposed（只能hook住java层）
        - 工具 Fdex2 ：Hook ClassLoader loadClass方法
        - 通用脱壳  dumpDex：https://github.com/WrBug/dumpDex
- 反编译