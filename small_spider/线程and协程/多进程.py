import random
from time import sleep
from multiprocessing import Process


def func(name):
    s = random.randint(1, 5)
    print(f'current process is {name}, sleeping {s}s.')
    sleep(s)
    print(f'process {name} is over')


if __name__ == '__main__':
    plist = []
    for i in range(1, 5):
        p = Process(target=func, args=(i,))  # args: 函数的参数 , 元组中只包含一个元素时，需要在元素后面添加逗号
        p.start()  # 启动子进程
        plist.append(p)
    for p in plist:
        p.join()  # 阻塞主进程
    print('main process')
    print('do something')

    p1 = Process(target=func, args=('daemon',))

    # 守护进程会在主进程结束后就会终止（不管守护进程的任务是否执行完毕）
    # 守护进程内无法开启子进程，否则抛出异常
    # p1.daemon = True  # 设置p1为守护进程,
    p1.start()  # 启动守护进程



## ------------------- 继承调用 -------------------
class Func(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        s = random.randint(1, 5)
        print(f'current process is {self.name}, sleeping {s}s.')
        sleep(s)
        print(f'process {self.name} is over')


if __name__ == '__main__':
    for i in range(1, 5):
        p = Func(str(i))
        p.start()
    print('main process')