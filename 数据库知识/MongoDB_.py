
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 或者
# myclient = pymongo.MongoClient('127.0.0.1', 27017)

## 1、创建数据库test
test_db = myclient["test_db"]
test_db.authenticate('user', 'password')  ## pymongo3.9版本及以前
## myclient = pymongo.MongoClient('mongodb://jieyang:970706@47.101.158.121:27017/test_db')  ## pymongo4.0


# 【注意】: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。

# 查看所有的数据库
dblist = myclient.list_database_names()

## 2、创建集合（表）sites
mycol = test_db["sites"]
## 或者不用单独创建，直接 xxx_db.xxx_col.insert_one() 会自动创建集合

# 【注意】: 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。

## 可设置数据过期时间，见 非关系性数据库.md

# 查看所有的集合
collist = test_db.list_collection_names()

## 3、增

# 3.1 集合(表)中插入一个文档(记录行)使用 insert_one() 方法
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)  # 返回InsertOneResult 对象
print(x.inserted_id)  # 如果我们在插入文档时没有指定 _id，MongoDB 会为每个文档添加一个唯一的 id

# 3.2 插入多个文档, 使用 insert_many() 方法
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)  # 输出插入的所有文档对应的 _id 值

# 3.3 插入指定 _id 的多个文档
mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]
x = mycol.insert_many(mylist)

## 4、删

# 4.1 删除一个文档
myquery = {"name": "Taobao"}
mycol.delete_one(myquery)  # 删除mycol中 name 字段值为 "Taobao" 的文档

# 4.2 删除多个文档
myquery = {"name": {"$regex": "^F"}}
xx = mycol.delete_many(myquery)  # 删除所有 name 字段中以 F 开头的文档
print(x.deleted_count, "个文档已删除")  # 查看被删除文档的个数

# 4.3 删除集合中的所有文档
x = mycol.delete_many({})

# 4.4 删除集合
mycol.drop()  # 如果删除成功 drop() 返回 true，如果删除失败(集合不存在)则返回 false

## 5、改

# 5.1 修改第一条, update_one() 如果查找到的匹配数据多于一条，则只会修改第一条
myquery = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}

mycol.update_one(myquery, newvalues)  # 将 alexa 字段的值 10000 改为 12345

# 5.2 修改所有匹配到的记录
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}

xs = mycol.update_many(myquery, newvalues)  # 查找所有以 F 开头的 name 字段, 并将匹配到所有记录的 alexa 字段修改为 123

print(x.modified_count, "文档已修改")  # 查看被修改文档的个数


## 6、查

# 6.1 查询集合中的第一条数据
x = mycol.find_one()

# 6.2 查询集合中的所有数据
for x in mycol.find():
  print(x)

# 6.3 查询指定字段的数据
# 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都默认为 1
for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):  # 1 表示查询此字段
  print(x)

# 除了 alexa 字段外，其他都返回：
for x in mycol.find({}, {"alexa": 0}):
  print(x)

# 6.4 根据指定条件查询
myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)  # 查找 name 字段为 "RUNOOB" 的数据

myquery = {"name": {"$gt": "H"}}
mydoc = mycol.find(myquery)  # 读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"}

# 6.5 使用正则表达式查询
myquery = {"name": {"$regex": "^R"}}
mydoc = mycol.find(myquery)  # 读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"}

# 6.6 返回指定条数记录
myresult = mycol.find().limit(3)  # 返回 3 条文档记录


## 7、排序

# sort() 方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序
mydoc = mycol.find().sort("alexa", -1)  # 对字段 alexa 按降序排序
for x in mydoc:
  print(x)
