## 去掉字符串末尾的空格和换行符
- str.strip()

## json模块
- json.dumps(dict_json) : 将 Python 对象编码成 JSON 字符串，同js中的`JSON.stringify(dict_json)`
- json.loads(dict_str) : 将 JSON 字符串解码为 Python 对象，同js中的`JSON.parse(dict_str)`
```python
import json
dict_json = {"a": 1, "b": {"list": [1, 2, 3], "str": "测试"}, "c": 3}
format_json = json.dumps(dict_json, ensure_ascii=False)  # (ensure_ascii=False 解决中文乱码)
print(format_json)  # 字符串

dict_str = '{"a": 123, "b": 456, "c": "测试"}'
print(json.loads(dict_str))  # 字典
```

- json.dump(json_dict, file_object, ensure_ascii=False) : 将字典写进文件 
- json.load(file_object)  ： 读取文件中的数据并转为字典
```python
import json
json_dict = {"a": 123, "b": 456, "c": "测试"}
file_object = open('why.json', 'w', encoding="utf8")
json.dump(json_dict, file_object, ensure_ascii=False)  # (ensure_ascii=False 解决中文乱码)

file_object = open('why.json', 'r', encoding="utf8")
info = json.load(file_object)
print(info)  # 字典
```

## 字节、编码
- 汉字在 GBK/GB2312 编码中占用 2 个字节，而在 UTF-8 编码中一般占用 3 个字节，英文数字占 1 个字节
- 编码方式：
    - GBK: 中文版本的编码(兼容中文和英文)
    - Unicode: 
        - 支持全球所有语言; 可以跟各种语言的编码自由转换，也就是说，即使你gbk编码的文字 ，想转成unicode很容易
        - Unicode只是规定了字的代号，也就是对应的映射关系，比如‘你‘的代号是12345，那么怎么编码这个值，才涉及到占几个字节（如：UTF-8 编码中一般占用 3 个字节）
        - 但有时又会说Unicode编码占几个字节，一般是2个字节
        - Unicode一般只用于内存中的编码使用
    - UTF-8：
        - 为了解决存储和网络传输的问题，出现了Unicode Transformation Format，学术名UTF，即：对unicode字符进行转换，以便于在存储和网络传输时可以节省空间
        - 使用1、2、3、4个字节表示所有字符；优先使用1个字符、无法满足则使增加一个字节，最多4个字节。英文占1个字节、欧洲语系占2个、东亚占3个，其它及特殊字符占4个
    
    - Base64:
        - 是什么？ 
            - Base64是一种用64个字符来表示任意二进制数据（如一张图片）的方法
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

- python中的编码问题
    - 【参考1】https://www.cnblogs.com/yyds/p/6171340.html
        【参考2】https://zhuanlan.zhihu.com/p/40834093
    - 文件存储encoding是怎样的，就要用相同的encoding去解。如果没指定，就用系统默认。所谓的encoding其实也就是字符集的mapping表而已
    - 磁盘上的文件都是以二进制格式存放的，其中文本文件都是以某种特定编码的**字节**形式存放的
    - 编码(encode)：将Unicode字符串转换成字节串（指定的编码方式）的过程和规则
    - 解码(decode)：将字节串（指定的编码方式）转换为对应的Unicode字符串(中的代码点)的过程和规则
    - python中的编码解码都是 Unicode字符串 与 字节串之间的转换
        ```python
        #!/usr/bin/env python
        '''
        比如我们使用Pycharm来编写Python程序时会指定工程编码和文件编码为UTF-8，
        那么Python代码被保存到磁盘时就会被转换为UTF-8编码对应的字节（encode过程）后写入磁盘。
        当执行Python代码文件中的代码时，Python解释器在读取Python代码文件中的字节串之后，
        需要将其转换为UNICODE字符串（decode过程）之后才执行后续操作。
        此句即为decode的格式。
        '''
        # -*- coding:utf-8 -*-
        
        import chardet
        
        a = "小甲"  # unicode字符串
        # print(chardet.detect(a))  # 这里会报错，因为只能传入字节型数据
        b = a.encode('utf-8')  # 以utf-8方式编码成字节
        print(chardet.detect(b))  # {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
        print(type(b))  # <class 'bytes'>
        c = b.decode('utf-8')  # 以utf-8方式解码成unicode字符串
        print(type(c))  # <class 'str'>
        ```
        ```python
        # 假设手动新建此txt文件且其中有中文，是保存在windows上的，则默认是gbk编码
        # 若open时不声明编码方式，则使用系统默认的编码方式（windows中为gbk，linux中是utf-8）
        # 问题：open中的encoding是在什么时候起作用（磁盘上的已经是编码后的字节数据了，为啥还要编码）
        with open('./requirements.txt', 'r', encoding='utf-8') as f:
            a = f.read()
            print(a)
            print(type(a))
        ```

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

## os模块
- 简介：操作系统接口模块
  - 与 sys模块 的区别
    - os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;
      sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境
- 使用
- 1）查看操作系统信息
```python
import os
print(os.name)  # posix
info = os.uname()
print(info)  # posix.uname_result(sysname='Darwin', nodename='jiedeMacBook-Pro.local', release='20.3.0', version='Darwin Kernel Version 20.3.0: Thu Jan 21 00:06:51 PST 2021; root:xnu-7195.81.3~1/RELEASE_ARM64_T8101', machine='x86_64')
print(info.sysname)  # Darwin
print(info.nodename)  # jiedeMacBook-Pro.local

print(os.sep)  # 当前系统路径的分隔符
```

- 2）os 执行cmd命令
```python
import os
# os.system
# os.system是简单粗暴的执行cmd指令，如果想获取在cmd输出的内容，是没办法获到的
os.system('pip install requests')

# os.popen
# 如果想获取控制台输出的内容，那就用os.popen的方法，popen返回的是一个file对象，跟open打开文件一样操作了，r是以读的方式打开
f = os.popen(r"python ./hello.py", "r")
d = f.read()  # 读文件
print(d)
print(type(d))
f.close()

```

- 3）文件路径相关
```python
import os
#  生成绝对路径
print(os.path.abspath('data.txt'))
print(os.path.abspath('hello.png'))

# 将2个路径合并成一个（不会判断有没有这个绝对路径）
print(os.path.join('/home/kiosk','hello.png'))  # 结果：/home/kiosk/hello.png
print(os.path.join(os.path.abspath('.'),'hello.jpg'))  # 当前路径下

# 获取当前路径
print (os.getcwd())

# 获取文件名或目录名
filename = ' /Users/jieyang/PycharmProjects/crawler_learn/spider_spa2.py'
print(os.path.basename(filename))  # spider_spa2.py
print(os.path.dirname(filename))  # /Users/jieyang/PycharmProjects/crawler_learn

# 返回目录下的所有文件和目录名
os.listdir()

# 创建目录/删除目录
os.mkdir('img')						##创建目录（若存在则创建失败）
os.makedirs('img/jpg/png')			##递归创建
os.rmdir('img')						##删除目录

# 创建文件/删除文件
os.mknod('aa.txt')  ##创建
os.remove('aa.txt')  ##删除

# 判断文件或目录是否存在
print(os.path.exists('data1.txt'))

# 判断是否是文件
print(os.path.isfile(filepath))

# 分离后缀名和文件名
print(os.path.splitext('hello.png'))  # ('hello', '.png')

# 将目录名和文件名分离
print(os.path.split('/tmp/hello/python.jpg'))  # ('/tmp/hello', 'python.jpg')


```

## 导入目录文件
- https://zhuanlan.zhihu.com/p/64893308
- 导入上级模块
```python
import sys 
# sys.path的作用：当使用import语句导入模块时，解释器会搜索当前模块所在目录以及sys.path指定的路径去找需要import的模块
sys.path.append("..") 
import xxx
```

## Python 直接赋值、浅拷贝和深度拷贝
- 【参考】https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
- 直接赋值：其实就是对象的引用（别名）。
- 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
- 深拷贝(deepcopy)： 完全拷贝了父对象及其子对象
```python
import copy
a = {1: [1, 2, 3]}
d = a
b = a.copy()
c = copy.deepcopy(a)
a[1].append(4)
print(a, d)  # {1: [1, 2, 3, 4]} {1: [1, 2, 3, 4]}
print(a, b)  # {1: [1, 2, 3, 4]} {1: [1, 2, 3, 4]}
print(a, c)  # {1: [1, 2, 3, 4]} {1: [1, 2, 3]}
```