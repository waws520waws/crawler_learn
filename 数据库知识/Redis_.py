import redis

## 1、连接数据库

# redis 取出的结果默认是字节, 可以设定 decode_responses=True 改成字符串
r = redis.StrictRedis(host='192.168.224.72', port=6379, password='123456', db=3, decode_responses=True)  # 连接本地编号为0的数据库

## 【注】：不同的值的类型有不同的操作方法，
# 可参考终端命令 https://www.runoob.com/redis/redis-keys.html， 大部分适用python中对redis的操作
# 或者参考python对redis的操作：https://www.runoob.com/w3cnote/python-redis-intro.html

## 2、对key的操作
r.randomkey()  # 随机获取一个键
r.delete(key1)  # 删除键

## 3、对string的操作

## 3.1 存数据
r.set('key1', 'sting1')
r.mset()  # 一次设置多个键值对

## 3.2 取数据
v = r.get('key1')
r.mget("k1", "k2")  # 一次取出多个键值对
print(v)
print(type(v))