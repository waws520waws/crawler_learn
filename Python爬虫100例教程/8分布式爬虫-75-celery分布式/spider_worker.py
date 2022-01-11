'''
此文件为：任务执行单元（消费者、workers）
'''

from celery import Celery


# 生成celery对象，'tasks'相当于key，用于区分celery对象
# broker: 消息队列 （可以只在配置文件中设置）
# backend：存储结果  （可以只在配置文件中设置）
# include参数需要指定 任务模块，使任务处于被worker监听的状态
app = Celery('task1', broker='redis://@127.0.0.1:6379/2', backend='redis://@127.0.0.1:6379/3', include=['add_task'])

# 方式1：从单独的配置模块中加载配置
app.config_from_object('celeryconfig')

'''方式2：在本文件中也可以加入配置（推荐使用方式1）
app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
)
'''

