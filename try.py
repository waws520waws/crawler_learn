import redis

## 1、连接数据库

# redis 取出的结果默认是字节, 可以设定 decode_responses=True 改成字符串
r = redis.StrictRedis('127.0.0.1', port=6379, db=0, decode_responses=True)  # 连接本地编号为0的数据库

r.set('key3', 'sting3')