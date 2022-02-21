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
        p = Process(target=func, args=(i,))
        p.start()  # 启动子进程
        plist.append(p)
    for p in plist:
        p.join()  # 阻塞主进程
    print('main process')
    print('do something')

    p1 = Process(target=func, args=('daemon',))
    p1.daemon = True  # 设置p1为守护进程
    p1.start()  # 启动守护进程