
'''
数据写入excel
'''

import xlwt

# workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个文件
# worksheet = workbook.add_sheet('sheet1')  # 创建工作表
# worksheet.write(0, 0, 'hello')  # 写入位置及数据
# workbook.save('table1.xls')


'''
数据写入json
'''
import requests
import json

if __name__ == '__main__':
    url = 'https://news.baidu.com/'

    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    req = requests.get(url, headers=head)

    # json返回的是obj（响应数据是json类型的，才可以使用json()）
    # text: 字符串；
    # content：二进制（如图片）；
    # json()：json对象
    dic_obj = req.json()

    fp = open('./file.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)