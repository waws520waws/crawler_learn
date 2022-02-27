import sys
sys.path.append(".")
# 导入 logging_logger.py 模块
from logging_logger import logger
# 使用
logger.debug('This is a debug')
logger.info('This is a info')
logger.warning('This is a warning')
logger.error('This is a error')
logger.critical('This is a critical')
