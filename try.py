import os
filename = ' /Users/jieyang/PycharmProjects/crawler_learn/try.py'


f = os.popen(r"python ./try2.py", "r")
d = f.read()  # 读文件
print(d)
print(type(d))
f.close()