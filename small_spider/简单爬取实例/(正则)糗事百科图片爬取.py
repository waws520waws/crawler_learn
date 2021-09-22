# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/

import requests
import re
import os
if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/imgrank/'

    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36'
    }

    page_text = requests.get(url, headers=header).text

    # 有（），则返回（）里的内容，无的话，则全部返回
    ex = r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

    img_src = re.findall(ex, page_text, re.S)


    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('picture_eg'):
        os.mkdir('picture_eg')

    for src in img_src:
        src = 'https:' + src
        # 图片的二进制数据（用content）
        img_data = requests.get(src, headers=header).content
        # 以路径的最后作为图片名称
        img_name = src.split('/')[-1]
        # 图片存储路径
        img_path = './picture_eg/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)



