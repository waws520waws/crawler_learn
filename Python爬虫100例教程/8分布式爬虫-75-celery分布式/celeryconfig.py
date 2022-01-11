CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

"""
CELERY_IMPORTS: 配置导入哥哥任务的代码模块
CELERY_QUEUES: 定义任务执行的各个任务队列（如按照执行时间分slow、fast等），默认有一个队列，暂称为一般任务队列。
CELERY_ROUTES: 配置各个任务分配到不同的任务队列
CELERY_SCHEDULE: 配置各个任务执行的时机参数

CELERY_TIMEZONE: 设置时区
CELERY_ENABLE_UTC: 是否启动时区设置，默认值是True
CELERY_CONCURRENCY: 并发的worker数量
CELERY_PREFETCH_MULTIPLIER: 每次去消息队列读取任务的数量，默认值是4
CELERY_MAX_TASKS_PRE_CHILD: 每个worker执行多少次任务后会死掉
BROKER_URL: 使用redis作为任务队列
CELERY_TASK_RESULT_EXPIRES: 任务执行结果的超时时间
CELERY_TASK_TIME_LIMIT: 单个任务运行的时间限制，超时会被杀死，不建议使用该参数，而用CELERY_TASK_SOFT_TIME_LIMIT
CELERY_RESULT_BACKEND: 使用redis存储执行结果
CELERY_TASK_SERIALIZER: 任务序列化方式
CELERY_RESULT_SERIALIZER: 任务执行结果序列化方式
CELERY_DISABLE_RATE_LIMITS: 关闭执行限速
"""
