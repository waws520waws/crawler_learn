#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Log Level如下，严重等级为NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL, 严重程度依次递增
若设置级别为DEBUG，则会将DEBUG级别以上的信息都输出显示再控制台上

logging.handlers.TimedRotatingFileHandler方法的参数说明如下：

filename: 是输出日志文件名

when: 是一个字符串的定义如下：
    “S”: Seconds
    “M”: Minutes
    “H”: Hours
    “D”: Days
    “W”: Week day (0=Monday)
    “midnight”: Roll over at midnight

interval: 是指等待多少个单位when的时间后，Logger会自动重建文件，当然，这个文件的创建
取决于filename+suffix，若这个文件跟之前的文件有重名，则会自动覆盖掉以前的文件，所以
有些情况suffix要定义的不能因为when而重复。

backupCount: 是保留日志个数。默认的0是不会自动删除掉日志。若设10，则在文件的创建过程中
库会判断是否有超过这个10，若超过，则会从最先创建的开始删除。
"""

import logging
import logging.handlers

# create formatter 创建一个格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 创建一个处理器ch 将日志输出到控制台
ch = logging.StreamHandler()
# 给处理器写入日志文件的 日志级别
ch.setLevel(logging.ERROR)
# 创建一个处理器ch2 将日志输出到文件，并按天分割日志
ch2 = logging.handlers.TimedRotatingFileHandler('./log/logging.log', when='D', interval=1, backupCount=30)
# 给处理器写入日志文件的 日志级别
ch2.setLevel(logging.DEBUG)


# 将格式器设置给处理器
ch.setFormatter(formatter)
ch2.setFormatter(formatter)


# 创建日志对象 记录器
logger = logging.getLogger(__name__)
# 设置日志对象的输出日志级别.处理器中设置日志级别时以处理器中的设置优先
logger.setLevel(logging.DEBUG)


# 将处理器设置给日志对象 记录器
# The final log level is the higher one between the default and the one in handler
logger.addHandler(ch)
logger.addHandler(ch2)
