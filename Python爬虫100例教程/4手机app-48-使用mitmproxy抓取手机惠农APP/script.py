
'''

启动 mitmproxy 后访问 http://httpbin.org/get 看代理是否生效
'''

from mitmproxy import ctx
import json
import pymongo

# 修改UA
# def request(flow):
#     #flow.request.headers['User-Agent'] = 'MitmProxy'
#     print(flow.request.headers)


def response(flow):
    start_url = "https://appapi.cnhnb.com/recq/api/transform/supply/selective/sapling"
    response = flow.response
    info = ctx.log.info
    if flow.request.url.startswith(start_url):
        text = response.text

        data = json.loads(text)
        save(data)


def save(data):
    DATABASE_IP = '127.0.0.1'
    DATABASE_PORT = 27017
    DATABASE_NAME = 'eg_100_db'
    client = pymongo.MongoClient(DATABASE_IP, DATABASE_PORT)
    db = client[DATABASE_NAME]
    collection = db.huinong  # 准备插入数据
    print(data["data"]["datas"])
    collection.insert_many(data["data"]["datas"])


