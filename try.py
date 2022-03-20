import requests
import json

HOT_SEARCH_URL = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/'
user_url = 'https://www.douyin.com/aweme/v1/web/tab/feed/'

HEADERS = {
    'user-agent': 'okhttp3'
}
QUERIES = {
    'device_platform': 'android',
    'version_name': '13.2.0',
    'version_code': '130200',
    'aid': '1128'
}
# QUERIES = {
#     'device_platform': 'PC',
#     'aid': '6383',
#     'count': 10,
#     'refresh_index': 2,
#     'video_type_select': 0,
#     'version_code': '170400',
#     'version_name': '17.4.0',
#     'cookie_enabled': 'true',
#     'screen_width': 1920,
#     'screen_height': 1080,
#     'browser_language': 'zh-CN',
#     'browser_platform': 'Win32',
#     'browser_name': 'Chrome',
#     'browser_version': '96.0.4664.110',
#     'browser_online': 'true',
#     'engine_name': 'Blink',
#     'engine_version': '96.0.4664.110',
#     'os_name': 'Windows',
#     'os_version': 10,
#     'cpu_core_num': 4,
#     'device_memory': 8,
#     'downlink': 10,
#     'effective_type': '4g',
#     'round_trip_time': 50,
#     'webid': '7068283311605581352'
# }

req = requests.get(HOT_SEARCH_URL, params=QUERIES, headers=HEADERS)
print(req.json())
# obj = json.loads(req.text)
# word_list = obj['data']['word_list']
# items = [item for item in word_list]
#
# for item in items:
#     print(item)