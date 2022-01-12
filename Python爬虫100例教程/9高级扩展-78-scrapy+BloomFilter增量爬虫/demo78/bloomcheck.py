'''
通过BloomFilter 类，去操作一个文件，实现去重，
这个地方注意一下，BloomFilter是通过读写文件的方式进行去重，如果你编写多进程或者多线程爬虫，使用的时候需要添加互斥和同步条件，
还有, BloomFilter涉及文件I/O操作，注意 批量写入 和 批量读取，否则效率会有很大的影响（也就是不要频繁的I/O）。
'''


from pybloom_live import BloomFilter
import os
import hashlib


class BloomCheck(object):
    def __init__(self):
        '''
        判断bf布隆文件是否存在，存在打开，不存在新建
        '''

        self.filename = 'bloomfilter.bf'
        is_exist = os.path.exists(self.filename)
        if is_exist:
            self.bf = BloomFilter.fromfile(open(self.filename, 'rb'))
        else:
            # capacity是必选参数，表示容量
            # error_rate 错误率
            self.bf = BloomFilter(capacity=100000000, error_rate=0.001)

    def process_item(self, data):
        data_encode_md5 = hashlib.md5(data.encode('utf-8')).hexdigest()
        if data_encode_md5 in self.bf:
            # 数据已存在
            return False
        else:
            # 数据不存在，新增到bf文件中
            self.bf.add(data_encode_md5)
            return True

    def save_bloom_file(self):
        # 批量写入（这里是最后再保存）
        self.bf.tofile(open(self.filename, 'wb'))
