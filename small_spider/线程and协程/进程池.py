
## **************** 旧方法 ****************
import random
from time import sleep
from multiprocessing import Pool


def func(name):
    s = random.randint(1, 5)
    print(f'current process is {name}, sleeping {s}s.')
    sleep(s)
    print(f'process {name} is over')


if __name__ == '__main__':
    p = Pool(3)
    for i in range(1, 5):
        p.apply_async(func, (i,))
    p.close()
    p.join()
    print('main process')



## ——————————————————  新方法 ——————————————————————
from concurrent.futures import ProcessPoolExecutor
import time


def work(x):
    time.sleep(2)
    return result


# Parallel implementation
with ProcessPoolExecutor() as pool:
    results = pool.map(work, (50, 100, 150, 200))
    for result in results:
        # 查看future代表的任务返回的结果
        print(result)

# 也可以像 线程池 那样可以使用 pool.submit() 手动提交单个任务
