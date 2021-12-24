## 去掉字符串末尾的空格和换行符
- str.strip()

## 字节、编码
- 汉字在 GBK/GB2312 编码中占用 2 个字节，而在 UTF-8 编码中一般占用 3 个字节，英文数字占 1 个字节
- 编码方式：
    - GBK: 中文版本的编码(兼容中文和英文)
    - Unicode: 
        - 支持全球所有语言; 可以跟各种语言的编码自由转换，也就是说，即使你gbk编码的文字 ，想转成unicode很容易
        - 一般用 **2个字节** 表示1个字符
    - UTF-8：
        - 为了解决存储和网络传输的问题，出现了Unicode Transformation Format，学术名UTF，即：对unicode字符进行转换，以便于在存储和网络传输时可以节省空间
        - 使用1、2、3、4个字节表示所有字符；优先使用1个字符、无法满足则使增加一个字节，最多4个字节。英文占1个字节、欧洲语系占2个、东亚占3个，其它及特殊字符占4个
    
    - Base64:
        - 是什么？ 
            - Base64是一种用64个字符来表示任意二进制数据的方法
        - 作用：
            - 由于某些系统中只能使用ASCII字符。Base64就是用来将非ASCII字符的数据转换成ASCII字符的一种方法
            - 例子：举个简单的例子，你使用SMTP协议 （Simple Mail Transfer Protocol 简单邮件传输协议）来发送邮件。因为这个协议是基于文本的协议，所以如果邮件中包含一幅图片，
              我们知道图片的存储格式是二进制数据（binary data），而非文本格式，我们必须将二进制的数据编码成文本格式，这时候Base 64 Encoding就派上用场了
        - base64特别适合在http，mime协议下快速传输数据
    
- 计算机系统通用的字符编码工作方式
    - 在 **计算机内存** 中，统一使用Unicode编码，当需要 **保存到硬盘** 或者需要 **传输** 的时候，就转换为UTF-8编码。
    - 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。
    
- python3.x：
    - 有两种数据类型，str和bytes；str类型存unicode数据，bytes类型存bytes数据
    - 文本总是unicode，由str类型表示，二进制数据则由bytes类型表示
    
## 转码
- 字符 与 Unicode编码 互转
    - 1、字符 转化为 Unicode编码 方法：`ord("A")`
    - 2、Unicode编码 转化为 字符 方法：`chr(65)`
- 字节 转 字符串
```python
import chardet
response = requests.get(url=url, headers=headers).content  # 得到字节
# chardet.detect() 函数接受一个参数，一个非unicode字符串， 它返回一个字典， 其中包含自动检测到的字符编码和从0到1的可信度级别。
charset = chardet.detect(response).get('encoding')  # 得到编码格式, {'confidence': 0.98999999999999999, 'encoding': 'GB2312'}
# bytes.decode(encoding=, errors=), 该函数返回字符串。换句话说是bytes类型转化成str类型的函数
# encoding规定解码方式。bytes数据是由什么编码方式编码的，该函数encoding参数就必须用相应解码方式，这样才能返回正确字符串
response = response.decode(charset, "ignore")  # 解码得到字符串
```

## 字符串
- r" " : 的作用是去除转义字符
    - 即如果是"\n"那么表示一个反斜杠字符，一个字母n，而不是表示换行了
    
- b" " ：后面字符串是bytes 类型
    - 用处： 网络编程中，服务器和浏览器只认 bytes 类型数据。
    
- u"我是含有中文字符组成的字符串"
    - 作用： 后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
    
## 生产者-消费者模式
- 【参考】：https://blog.csdn.net/miaoqinian/article/details/80077388
- 含义：生产者（负责造数据），消费者（接收造出来的数据进行进一步的操作）
    - 一般是与多线程/多进程一起使用
    
- 为什么要使用生产者消费者模型？ 
    - 在并发编程中，如果生产者处理速度很快，而消费者处理速度比较慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，
      如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个等待的问题，就引入了生产者与消费者模型。让它们之间可以不停的生产和消费

- 实现生产者消费者模型三要素：
    - 1、生产者
    - 2、消费者
    - 3、队列（或其他的容哭器，但队列不用考虑锁的问题）
    
- 什么时候用这个模型？
    - 程序中出现明显的两类任务，一类任务是负责生产，另外一类任务是负责处理生产的数据的（如爬虫）
    
- 用该模型的好处？
    - 1、实现了生产者与消费者的解耦和
    - 2、平衡了生产力与消费力，就是生产者一直不停的生产，消费者可以不停的消费，因为二者不再是直接沟通的，而是跟队列沟通的。
    
## 日期
```python
from datetime import datetime, date, timedelta

yesterday = date.today() + timedelta(days = -1)    # 昨天日期
print(yesterday)  # datetime.date(2018-7-16)

# 可以选择格式化输出：
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")    # 昨天日期
print(yesterday)  # '2018-07-16'

import time
t = time.time()  # 当前时间的毫秒数
print(t)  # 1640244263.058194
```

## yield
- 【参考】https://blog.csdn.net/mieleizhi0522/article/details/82142856/
- 简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次再调用时就从这个位置后开始

## cls 、类方法
- cls代表的是类的本身，相对应的self则是类的一个实例对象
- 类方法需要使用 ＠classmethod 修饰符进行修饰
```python
class Person(object):
    def __init__(self, name, age):  # 带两参数
        self.name = name
        self.age = age
        print('self:', self)

    # 定义一个build方法，返回一个person实例对象，这个方法等价于 p = Person("Tom", 18)
    @classmethod
    def build(cls):
        # cls()等于Person()
        p = cls("Tom", 18)  # 需带两参数
        print('cls:', cls)
        return p

if __name__ == '__main__':
    person = Person.build()
    print(person, person.name, person.age)
```