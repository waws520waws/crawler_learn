## 1、scrapyd
- 【官方文档】https://scrapyd.readthedocs.io/en/stable/
- 简介：Scrapyd是一个网页版管理scrapy的工具，用来部署和运行Scrapy项目，由Scrapy的开发者开发。
- 使用
    - 【参考】https://dream.blog.csdn.net/article/details/108320733
    - 1、安装scrapyd：`pip install scrapyd`
        - cmd输入：`scrapyd` 运行
    - 2、创建scrapy项目
    - 3、安装scrapyd-client: `pip install scrapyd-client`
    - 4、Linux或者Mac可以直接运行：`scrapyd-deploy -l`
        - windows需要做一些其他工作，才能运行
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
            