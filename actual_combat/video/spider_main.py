'''
一般的视频网站是怎么做的？
- 用户上传 -> 转码（把视频做处理，标清，高清，2k）-> 切片处理（把大文件拆分成.ts小文件）
- 需要一个文件来记录这些文件：1。视频播放顺序，2。视频存放的路径
    - 这种文件一般是文本文件：M3U，M3U8(utf-8)，txt，json

- 抓取一个视频的步骤：
    - 1、找到m3u8文件（各种手段）
    - 2、通过m3u8下载ts切片文件【可能存在加密，需要先解密】
    - 3、可以通过各种手段（不仅是编程手段）把ts文件合并成一个mp4文件
'''

'''
此案例思路：
    1、请求原始url，拿到js链接
    2、请求js链接，拿到视频链接
    3、请求视频链接，找到m3u8文件
    4、两次请求m3u8链接
    5、拿到ts文件
    6、拿到密匙
    7、解密ts文件
    8、合并ts文件为mp4文件
'''

import re

import requests


# 请求js地址，解析出video的url
def get_video_url(url):
    req = requests.get(url).text
    cmp = re.compile('HD\$(?P<video_url>.*?)\$yjyun', re.S)
    video_url = cmp.search(req).group('video_url')  # https://v10.dious.cc/share/ZfhOMGgRqg0EHo2S
    print('video_url: ', video_url)
    return video_url


# 对原始url发起请求，观察页面，解析出js地址
def get_video_url_js(url):
    req = requests.get(url).text
    cmp = re.compile('l player.*?src="(?P<video_url>/playdata.*?)">', re.S)
    video_url_js = cmp.search(req).group('video_url')  # /playdata/81/184401.js?3110.984

    video_url_js = url.split('/xj')[0] + video_url_js
    print('video_url_js: ', video_url_js)
    video_url = get_video_url(video_url_js)
    return video_url


def get_m3u8_url(url):
    req = requests.get(url).text
    cmp = re.compile('main = "(?P<m3u8_url>)";', re.S)
    m3u8_url = cmp.search(req).group('m3u8_url')  # /20210923/F9kgfyAW/index.m3u8
    m3u8_url = url.split('/share')[0] + m3u8_url
    print('m3u8_url: ', m3u8_url)
    return m3u8_url


def main(url):
    video_url = get_video_url_js(url)
    m3u8_url = get_m3u8_url(video_url)


if __name__ == '__main__':
    url = 'https://www.ywtx360.com/xj/184401/player-0-0.html'
    main(url)
