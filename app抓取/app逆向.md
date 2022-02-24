## APP逆向
- 【安卓逆向的一些工具】https://zhuanlan.zhihu.com/p/313886157
- 关于逆向的文章：去看雪论坛或者吾爱破解论坛吧，哪里有太多的文章

### 3.1 绕过证书验证类
- 简介：打开 fiddler 先来抓个包，fiddler 开启之后 app提示连接不到服务器，发现这个 app 做了证书验证
- 解决这种问题一般都是安装 xposed 框架，里面有一个 JustTrustme 模块，它的原理就是hook，直接绕过证书验证类
    - 注意事项：
        - 手机必须获取root权限
        - 安装xposed框架有手机变成砖块的危险（因为会改变系统文件）
            - 手机可以直接刷带有Xposed框架的系统（如：刷机精灵）

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
                - 要先安装java
                - 最新2.1版本下载地址：https://github.com/pxb1988/dex2jar/releases
                    - 用之前的版本在转换时会报错：`Detail Error Information in File .\classes-error.zip`
                - 一次转换多个文件：`d2j-dex2jar.bat classes2.dex classes3.dex classes4.dex`
            - jd-gui: 这个工具用于查看源码（此工具将jar文件转换成java代码）
          
        - 根据请求或响应的参数去源码中搜索需要的东西（如：加密方式）
            - 【**阅读代码技巧**】
                - 需要注意的是，反编译的代码非常混乱，错误很多，并且apk经过混淆，变量名都消失了，这时一定要有有耐心，仔细研究代码。
                - 根据前面请求、响应参数去搜索，或者请求的 url 地址去搜索，而且经验很重要。
                - 如果不知道生成的方式，就用 java运行一波，将这两个参数打印出来
                - 一个技巧：可以使用 xposed 写一个 hook代码 把参数打印出来；或者 使用 frida 来写一段 hook 代码
                    - 【参考】https://www.cnblogs.com/yhoil/articles/14705792.html
                - 一般先从最大的文件开始依次搜索关键字
            - 【加密参数定位方法】
                - 【参考】https://blog.csdn.net/weixin_43582101/article/details/115355563
                - 静态分析：使用工程搜索检索需要查找的参数名
                - 动态分析：
                    - objection定位
                      - 在通过搜索之后如果有几个不确定的位置，则可以使用Objection
                    - frida-hook
                      - 通过frida凭感觉Hook下App中所有操作Base64的位置
                    - log注入
                      - 流程是先修改apk的smali代码，既是在某关键函数前加入 android/util/Log 输出，配合LogCat 查看程序执行时的log数据；
                        一般使用Log.v() 日志输出函数就可以了。
        
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
    - 通常是看lib文件夹下so库特征，以下是市面上常见的不同厂商对APP的加固特征：
        - 爱加密：libexec.so,libexecmain.so，ijiami.dat
        - 梆梆： libsecexe.so,libsecmain.so , libDexHelper.so libSecShell.so
        - 360：libprotectClass.so,libjiagu.so，libjiagu_art.so，libjiagu_x86.so
        - 百度：libbaiduprotect.so
        - 腾讯：libshellx-2.10.6.0.so，libBugly.so，libtup.so, libexec.so，libshell.so，stub_tengxun
        - 网易易盾：libnesec.so

- 查壳工具：
    - ApkScan-PKID
      - 下载地址：https://www.jianshu.com/p/dbea956c64aa
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

