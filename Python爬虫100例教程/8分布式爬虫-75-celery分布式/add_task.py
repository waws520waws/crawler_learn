'''
任务加入到 broker 队列中，以便刚才我们创建的 worker 能够从队列中取出任务并执行
当启动worker时，以下三个task同时进入监听状态
'''

from spider_worker import app
import requests
from lxml import etree

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17"
}


@app.task
def main_task(url):
    # 主函数
    print("main 函数运行")
    run.delay(url)


@app.task
def run(url):
    # 发送请求
    print("run 函数运行")
    try:
        res = requests.get(url, headers=headers)
        get_detail.delay(res.text)  # 将标签页源码加载到列表中
    except Exception as e:
        print(e)


@app.task
def get_detail(html):
    print("get_detail函数运行")
    if not html:
        return None
    # 解析标签页详细数据
    et = etree.HTML(html)
    tags = et.xpath("//table[@class='tagCol']/tbody/tr/td/a/text()")
    result = []
    for tag in tags:
        tag_url = f"https://book.douban.com/tag/{tag}"
        tag_res = requests.get(tag_url, headers=headers)
        tag_et = etree.HTML(tag_res.text)
        title_result = tag_et.xpath("//div[@class='info']/h2/a/@title")
        result.extend(title_result)
        print(result)  # 最后的结果并未保存入库，直接输出了
        return result  #


"""
返回值：
    <AsyncResult: 622a4133-9187-41f5-88f3-b259893af13f>：这个对象可以用来检查任务的状态或者获得任务的返回值。

"""