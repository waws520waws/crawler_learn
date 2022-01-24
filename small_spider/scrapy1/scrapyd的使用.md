## 1、scrapyd
- 【官方文档】https://scrapyd.readthedocs.io/en/stable/
- 简介：Scrapyd是一个网页版管理scrapy的工具 (相当于一个组件)，用来部署和运行Scrapy项目，由Scrapy的开发者开发。
- 使用
    - 【参考】https://dream.blog.csdn.net/article/details/108320733
    - 1、安装scrapyd：`pip install scrapyd`
        - cmd输入：`scrapyd` 运行
    - 2、创建scrapy项目
    - 3、安装scrapyd-client: `pip install scrapyd-client`
        - scrapyd-client模块是专门打包scrapy爬虫项目到scrapyd服务中的
    - 4、Linux或者Mac可以直接运行：`scrapyd-deploy -l`
        - windows需要做一些其他工作，才能运行（见【参考】链接）
    - 5、修改scrapy项目下的 scrapy.cfg 文件
        - 解开url的注释
        - 将 `[deploy]` 修改为 `[deploy:target_name]`，如下：
            ```python
            [settings]
            default = firstScrapyd.settings
            
            [deploy:myfirst]
            url = http://localhost:6800/
            project = firstScrapyd
            ``` 
    - 6、运行命令将项目上传到scrapyd（需要先运行scrapyd）
        - `scrapyd-deploy target_name -p project_name`
        - target_name 为你的服务器命令，两个参数均在 scrapy.cfg 文件中配置好
    - 7、scrapyd 运行项目
        - `curl http://localhost:6800/schedule.json -d project=PROJECT_NAME -d spider=SPIDER_NAME`
            - 没有 curl命令的，需要安装；SPIDER_NAME 不加文件后缀
            - windows运行此命令可能会报错，根据报错提示解决它
        - 其他控制命令见官方文档
            - 获取状态、
            - 获取项目列表、
            - 获取项目下已发布的爬虫列表、
            - 获取项目下已发布的爬虫版本列表
            - 获取爬虫运行状态
            - 启动服务器上某一爬虫（必须是已发布到服务器的爬虫）
            - 删除某一版本爬虫
            - 删除某一工程，包括该工程下的各版本爬虫
    - 8、修改配置文件，允许外网访问
        - scrapyd包 路径下的 default_scrapyd.conf 文件：
            - 将文件中的 bind_address 改为 `0.0.0.0`(所有均可访问) 或者 指定某个ip
         
## 2、scrapydweb
- （爬虫管理平台）是一个美化scrapyd的可视化组件，集成并且提供 更多 可视化功能和 更优美 的界面。
  采用 Flask+VUE 实现。
- 【总结】scrapy、scrapyd、scrapydweb三者如同葫芦套娃，总共三层
- 【github地址】https://github.com/my8100/files/tree/master/scrapydweb
- 使用
    - 【参考】https://dream.blog.csdn.net/article/details/108325969
    - 安装scrapydweb：`pip install scrapydweb`
    - 运行scrapydweb：`scrapydweb` （需要先运行scrapyd）
        - 会在当前目录下生成 scrapydweb_settings_v10.py 文件
    - 打开上面的配置文件，进行配置
        - 由于是本地跑，所注释掉 `('username', 'password', 'localhost', '6801', 'group')`, 其中group是组名，可以吧scrapyd自动划分成组
        - 注意下面参数
            ```python
            ENABLE_AUTH = False
            # In order to enable basic auth, both USERNAME and PASSWORD should be non-empty strings.
            USERNAME = ''
            PASSWORD = ''
            ```
        - 配置项目路径（配置成项目所在目录的上一级目录）（绝对路径）
            - `SCRAPY_PROJECTS_DIR = '/Users/jieyang/PycharmProjects/crawler_learn/Python爬虫100例教程/9高级扩展-82-scrapyd/'`
            - 这里是scrapydweb比较方便的地方，不用事先将项目先上传到scrapyd服务器，scrapydweb能够帮我们上传
    - 重启scrapydweb
        - 需要进入到 scrapydweb_settings_v10.py 文件所在目录启动
    - 启动后可能会报一个警告 或者 访问 http://127.0.0.1:5000/ 时显示 'pip install logparser...'
        - 可以执行 `logparser -dir D:\...\project_name/logs` 用于记录日志
    - scrapydweb面板功能介绍
        - Servers ：         scrapyd server 服务器信息
        - Timer Tasks ：     定时任务
        - Jobs ：            任务信息，以及运行产生的日志信息
        - Deploy Project ：  部署项目
        - Send Text ：       可邮件通知爬取结果
        - 其他功能如：打开scrapyweb安全认证，开启https，可在配置文件中设置
    
- 其他爬虫管理平台
    - SpiderKeeper本篇博客待介绍的，基于 scrapyd，开源版的scrapyhub，同样不支持scrapy以外的爬虫。
    - Gerapy 采用 Django+VUE 实现，该平台国内大佬开发，UI美观，支持的功能与 Scrapydweb 类似。
    - Grawlab 采用 Golang+VUE 实现，该平台不局限于scrapy了，可以运行各种爬虫，不过部署比较复杂。