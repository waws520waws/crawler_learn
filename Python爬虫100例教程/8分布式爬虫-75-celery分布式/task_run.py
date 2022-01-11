'''
调用任务
'''

from celery import group
from celery import chain
from add_task import main_task
url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"

res = main_task.delay(url)  # delay() 给任务发送消息的简化写法，即 apply_async() 的简化写法
# my_task1.delay()
"""
调用任务:
    可以使用apply_async()方法，该方法可让我们设置一些任务执行的参数，
        例如，任务多久之后才执行，任务被发送到那个队列中等等.
    my_task.apply_async((2, 2), queue='my_queue', countdown=10)
        任务my_task将会被发送到my_queue队列中，并且在发送10秒之后执行。
    如果我们直接执行任务函数，将会直接执行此函数在当前进程中，并不会向broker发送任何消息。
    无论是delay()还是apply_async()方式都会返回AsyncResult对象，方便跟踪任务执行状态，但需要我们配置result_backend.
    每一个被调用的任务都会被分配一个ID，我们叫Task ID.
"""
# my_task2.apply_async(queue="queue1", countdown=10)

"""
一个signature包装了一个参数和执行选项的单个任务调用。我们可将这个signature传递给函数。
我们将my_task1()任务包装称一个signature:10秒后执行
"""
# t3 = my_task1.signature(countdown=10)
# t3.delay()


"""
Primitives:
    这些primitives本身就是signature对象，因此它们可以以多种方式组合成复杂的工作流程。primitives如下:
    group: 一组任务并行执行，返回一组返回值，并可以按顺序检索返回值。
    chain: 任务一个一个执行，一个执行完将执行return结果传递给下一个任务函数.

"""
# 将多个signature放入同一组中
# my_group = group((my_task4.s(11, 12), my_task5.s(1, 12), my_task6.s(11, 2)))
# ret = my_group()  # 执行组任务
# print(ret.get())  # 输出每个任务结果

"""
将多个signature组成一个任务链
my_task4的运行结果将会传递给my_task5
my_task5的运行结果会传递给my_task6
"""
# my_chain = chain(my_task4.s(10, 10) | my_task5.s(10) | my_task6.s(10))
# ret = my_chain()  # 执行任务链
# print(ret.get())  # 输出最终结果


"""
Routing（要写配置文件）
    假如我们有两个worker,一个worker专门用来处理邮件发送任务和图像处理任务，一个worker专门用来处理文件上传任务。
    我们创建两个队列，一个专门用于存储邮件任务队列和图像处理，一个用来存储文件上传任务队列。
    Celery支持AMQP(Advanced Message Queue)所有的路由功能，我们也可以使用简单的路由设置将指定的任务发送到指定的队列中.

"""
# my_task1.apply_async(queue='queue1')
# my_task3.apply_async(queue='queue2')

"""
Periodic Tasks:（要写配置文件）
    celery beat是一个调度器，它可以周期内指定某个worker来执行某个任务。
    如果我们想周期执行某个任务需要增加beat_schedule配置信息. 
    不能在windows上运行
    启动worker处理周期性任务(命令行):celery -A proj worker --loglevel=info --beat

    celery需要保存上次任务运行的时间在数据文件中，文件在当前目录下名字叫celerybeat-schedule. beat需要访问此文件：
        celery -A proj beat -s /home/celery/var/run/celerybeat-schedule
"""
