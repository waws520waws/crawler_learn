import pymongo

client = pymongo.MongoClient('47.101.158.121', 27017)
db = client['testdb']
db.authenticate('jieyang', '970706')
item = {'title': '  党历史自信的最大底气 '}
db['mytable1'].insert_one(item)