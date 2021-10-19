import json
book_id = 'asdasda'
cid = '12334433'
params = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
print(params)
print(type(params))
url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={params}'
print(url)

data = json.dumps(params)
print(data)
print(type(data))
url2 = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
print(url2)