import requests

url = 'https://antispider3.scrape.center/api/book/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

params = {
    'limit': 18,
    'offset': 0
}

res = requests.get(url, headers=headers, params=params)

print(res.text)