# !/usr/bin/python3

'''
参考：https://www.runoob.com/python3/python3-multithreading.html

提供的其他方法：
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
    setDaemon(): 设置某线程为守护线程【与 join() 方法对立】
        - 守护进程的两个特点
            守护进程会在主进程结束后就会终止（不管守护进程的任务是否执行完毕）；
            守护进程内无法开启子进程，否则抛出异常

'''
import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # 继承了threading.Thread类，必须实现run()方法
    def run(self):
        print("开启线程： " + self.name)
        '''
        称为'线程同步之 Lock (互斥锁)'：
            对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间
            因为如果多个线程共同对某个数据修改，则可能出现不可预料的结果。
            可用 队列 代替 互斥锁（主要用于生产者消费者模式，100例）
        '''
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

        # 也可以使用 with语句
        # with threadLock:
        #     print_time(self.name, self.counter, 3)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 设置thread1为守护线程
# thread1.daemon = True
# thread1.setDaemon(True)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成，才继续运行主进程后面的代码
for t in threads:
    t.join()
print("退出主线程")




############################################# 最简单实现
import threading
import time

def run(n):
    print("task", n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
##############################################

