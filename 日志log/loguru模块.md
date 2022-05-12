```python
from loguru import logger

aa = 'qwe'
print(aa)
logger.info('this is a info!!!')    # 2022-05-11 14:40:03.384 | INFO     | __main__:<module>:5 - this is a info!!!
logger.debug('this is a debug!!!')  # 2022-05-11 14:39:37.405 | DEBUG    | __main__:<module>:5 - this is a debug!!!
```