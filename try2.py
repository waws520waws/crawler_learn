

import pymongo
# myclient = pymongo.MongoClient('127.0.0.1', 27017)
# pic_db = myclient['pic_db']
# for x in pic_db.find():
#   print(x)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 或者
# myclient = pymongo.MongoClient('127.0.0.1', 27017)


## 1、创建数据库test
test_db = myclient["test_db"]


# 【注意】: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。

# 查看所有的数据库
# dblist = myclient.list_database_names()

## 2、创建集合（表）sites
mycol = test_db["sites"]

# 【注意】: 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。

# 查看所有的集合
# collist = test_db.list_collection_names()

## 3、增

# 3.1 集合(表)中插入一个文档(记录行)使用 insert_one() 方法
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)  # 返回InsertOneResult 对象
print(x.inserted_id)  # 如果我们在插入文档时没有指定 _id，MongoDB 会为每个文档添加一个唯一的 id