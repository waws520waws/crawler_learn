import requests
import time
from retrying import retry
import traceback

fail_url = []  # 请求失败的url

def parse_data(res):
    print('parse_data')

# wait_fixed: 设置重试间隔时长（ms）
@retry(stop_max_attempt_number=3, wait_fixed=1000)
def test_retry(url):
    try:
        res = requests.get(url)  # 这里可能会报连接超时等错误
    except Exception as e:
        time.sleep(2)
        # 同：traceback.print_exc(e)
        raise e
    else:
        if res.status_code == 200:
            fail_url.pop()  # 请求成功, 将此url移除
            parse_data(res)

def main():
    urls = ['', '']  # 待爬取url
    for url in urls:
        fail_url.append(url)  # 先默认请求失败，在请求成功时再将其移除
        test_retry(url)

main()