
'''
线程池与进程池模块：multiprocessing 与 concurrent.futures（Python3.2开始）
    concurrent.futures的性能并没有更好,只是让编码变得更简单。考虑并发编程的时候,任何简化都是好事。从长远来看,concurrent.futures编写的代码更容易维护

multiprocessing.dummy 是多线程模块；multiprocessing是多进程模块
'''


# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/


# 线程池的使用
    # 使用原则：线程池处理的是阻塞并且耗时的操作
    # 通过下面线程池的使用可以看出：需要将阻塞并且耗时的操作封装在一个函数中，再调用


## **************** 旧方法 ****************
import time
from multiprocessing.dummy import Pool

start_time = time.time()
def fn(s):
    print('starting...: ', s)
    time.sleep(2)
    print('end...:', s)


li = ['aa', 'bb', 'cc', 'dd']

# 实例化一个线程池（一般设置为操作系统核数4）
pool = Pool(4)

# 将list中每一个元素传递给fn进行处理
pool.map(fn, li)

# 关闭线程池
pool.close()

# 让主线程等待子线程结束后才关闭
pool.join()

end_time = time.time()
print('total spend time: ', end_time-start_time)


## ——————————————————  新方法 ——————————————————————
# 【参考】https://blog.csdn.net/pursuit_zhangyu/article/details/97925622
from concurrent.futures import ThreadPoolExecutor
import time


# 定义一个准备作为线程任务的函数
def action(max):
    time.sleep(2)
    return max


def get_result(future):
    print(future.result())


# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 50)
# 为future1添加线程完成的回调函数, 该回调函数会在线程任务结束时获取其返回值
future1.add_done_callback(get_result)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 100)

# 还提供了一个 map(func, *iterables, timeout=None, chunksize=1) 方法来提交任务；参数位置放的是可迭代对象
# 向线程池提交4个task, (50,100,150,200)会作为action()函数的参数
# results收集线程任务的返回值
results = pool.map(action, (50,100,150,200))

# 关闭线程池
pool.shutdown()


# 程序可以使用 with 语句来管理线程池，这样即可避免手动关闭线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池提交一个task, 50会作为action()函数的参数
    future1 = pool.submit(action, 50)
    # 查看future1代表的任务返回的结果
    print(future1.result())

