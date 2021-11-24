import requests
'''
- 需求：网易云课堂课程爬取
- 技术：带payload参数的请求
- URL：https://study.163.com/courses-search?keyword=%E7%88%AC%E8%99%AB
'''


def get_json():
    index = 1
    print(f"正在抓取{index}页数据")
    payload = {
        "pageIndex": index,
        "pageSize": 50,
        "relativeOffset": 50,
        "frontCategoryId": -1,
        "searchTimeType": -1,
        "orderType": 50,
        "priceType": -1,
        "activityId": 0,
        "keyword": ""
    }
    headers = {
        "Accept": "application/json",
        "Host": "study.数字.com",
        "Origin": "https://study.数字.com",
        "Content-Type": "application/json",
        "Referer": "https://study.数字.com/courses",
        "User-Agent": "自己去找个浏览器UA"
    }
    try:
        # 请注意这个地方发送的是post请求
        # CSDN 博客 梦想橡皮擦
        res = requests.post("https://study.数字.com/p/search/studycourse.json", json=payload, headers=headers)
        content_json = res.json()

    except Exception as e:
        print("出现BUG了")
        print(e)


def main():
    get_json()


if __name__ == '__main__':
    main()
