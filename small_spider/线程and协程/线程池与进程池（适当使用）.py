# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/


# 线程池的使用
    # 使用原则：线程池处理的是阻塞并且耗时的操作
    # 通过下面线程池的使用可以看出：需要将阻塞并且耗时的操作封装在一个函数中，再调用

import time
from multiprocessing.dummy import Pool

start_time = time.time()
def fn(s):
    print('starting...: ', s)
    time.sleep(2)
    print('end...:', s)


li = ['aa', 'bb', 'cc', 'dd']

## 实例化一个线程池（一般设置为操作系统核数4）
pool = Pool(4)

## 将list中每一个元素传递给fn进行处理
pool.map(fn, li)

## 关闭线程池
pool.close()

## 让主线程等待子线程结束后才关闭
pool.join()

end_time = time.time()
print('total spend time: ', end_time-start_time)