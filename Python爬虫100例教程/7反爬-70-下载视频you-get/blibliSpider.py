'''
需求：抓取blibli视频
技术：you-get, 抓包
'''

## 方法1：使用 you-get 模块
import requests

'''
import os
try:
    download = "you-get --format=flv https://www.bilibili.com/video/BV16a4y1e7r8?p=1"
    print(download)
    res = os.system(download)  #  os.system 方法：将字符串转化成命令在cmd上运行
    print(res)
    print("下载完成")
except Exception:
    print("视频下载出现了错误")
'''

## 方法2：利用抓包工具构造请求
'''
【参考教程】https://dream.blog.csdn.net/article/details/106546531
1、查看请求信息，可以看到 请求视频流文件的时候，是可以通过Range参数对视频请求大小进行控制的
2、那么可以通过抓包工具 拦截请求，修改请求参数（即修改Range参数），一次性将视频全部请求下来
3、保存
4、上面步骤可以作为分析原理，然后是写代码实现
'''
# 代码实现
'''
在抓包工具中发现：
    1、视频请求有 OPTION请求，状态码是200；有get请求，状态码是206；两者请求的url相同
    2、需要用到session保持会话
【注意】此案例只用于针对某一个 blibli 视频，进行下载，不通用（每一个视频下载都要修改参数？还未测）
      url具有时效性，需重新copy链接
'''

video_url = 'https://xy182x147x21x36xy.mcdn.bilivideo.cn:4483/upgcxcode/45/52/461865245/461865245_u1-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1641283964&gen=playurlv2&os=mcdn&oi=2883149043&trid=0001c1007def2d1f414f892dadecd7e171cfu&platform=pc&upsig=dad1f52c739470ad23d553698de3c6c3&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=2001680&mid=451044359&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=169186&logo=A0000002'

audio_url = 'https://xy182x134x198x81xy.mcdn.bilivideo.cn:4483/upgcxcode/45/52/461865245/461865245_u1-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1641283964&gen=playurlv2&os=mcdn&oi=2883149043&trid=0001c1007def2d1f414f892dadecd7e171cfu&platform=pc&upsig=21008e91a1f83d5216e541df532994c0&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=2001683&mid=451044359&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=40326&logo=A0000002'

option_headers = {
    'access-control-request-method': 'GET',
    'access-control-request-headers': 'range',
    'origin': 'https://www.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bilibili.com/video/BV1wZ4y1R7gH?spm_id_from=333.851.b_7265636f6d6d656e64.11',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9'
}


headers = {
    'accept': '*/*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9',
    'if-range': 'Fri, 31 Dec 2021 00:58:42 GMT',
    'origin': 'https://www.bilibili.com',
    'range': 'bytes=0-20471626',
    'referer': 'https://www.bilibili.com/video/BV1wZ4y1R7gH?spm_id_from=333.851.b_7265636f6d6d656e64.11',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}


session1 = requests.session()
session1.options(video_url, headers=option_headers, verify=False)
res = session1.get(video_url, headers=headers, verify=False)
print(res.status_code)
with open('./video.mp4', 'wb') as f:
    f.write(res.content)

session2 = requests.session()
session2.options(audio_url, headers=option_headers, verify=False)
res = session2.get(audio_url, headers=headers, verify=False)
print(res.status_code)
with open('audio.mp3', 'wb') as f:
    f.write(res.content)


## 方法3：去别人写好的网站下载
'''
在地址栏里bilibili前面加上一个“i”变成 ibilibili，然后回车。 浏览器将跳转到一个新页面，在这个页面，你就可以直接下来B站视频。
'''
