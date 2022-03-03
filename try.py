import hashlib
## ====================== bv
str1 = 'https://dream.blog.csdn.net/article/details/108225659'

# 1、创建hash对象
hl = hashlib.md5()

# 2、向hash对象中添加需要做hash运算的字符串
hl.update(str1.encode('utf-8'))  # 这个地方传的是bytes类型的数据，否则会报错

# 3、获取字符串的hash值
bv = hl.hexdigest()
print(bv)