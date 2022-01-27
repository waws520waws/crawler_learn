from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    # 1、os.path.abspath(path) 返回绝对路径
    # 2、os.path.dirname(path) 返回文件夹路径
    # 3、sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值， sys.path.append当前文件执行的目录的路劲就加入到python
    # 4、file 本文件的地址
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'tryspider'])