
'''
例67：第一次使用 tkinter，实现GUI的一个小例子
例68：例67的基础上，新增多线程，新增正则文本框
'''

import tkinter as tk
from tkinter import Tk
import requests
import re
import time

# 创建主窗口
win = Tk()

## 1、设置标题
win.title("抓图小程序")

## 2、窗体大小设置（居中显示）
width = 500
height = 400
# 获取屏幕分辨率
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
position = f"{width}x{height}+{(screen_width - width) / 2:.0f}+{(screen_height - height) / 2:.0f}"
win.geometry(position)
# 设置窗口大小与位置
# win.geometry('500x300+200+400')  # 500x300是窗口大小（注意这个x是字母x），200与400是窗口的位置

## 3、控件的使用
# 创建提示文本
# lb = tk.Label(win, text='请输入网址：', font=('黑体', 20), bg='white', width=, height=)
lb = tk.Label(win, text='请输入网址：')
# 创建文本框
entry = tk.Entry(win, width=30)  # width 设置文本框的宽度，以字符为单位，默认值是20
# 创建按钮, command: 绑定触发函数
# btn = tk.Button(win, text='分析下载', command=down_img)
# 创建一个多行文本框
t = tk.Text(win, width=60, height=20)
# t.insert("insert", f"开始下载图片...\n")


## 4、触发按钮事件
def down_img():
    url = entry.get()
    analyse(url)


btn = tk.Button(win, text='分析下载', command=down_img)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    "Referer": "https://img3.chinadaily.com.cn"
}


def analyse(url):
    resp = requests.get(url, headers=headers)
    content = resp.text  # 获取到网页内容
    # print(content)
    imgs = re.findall('img src="(.*?)"', content)

    # 界面展示获取到的图片数量
    t.insert("insert", f"获取到{len(imgs)}张图片\n")
    t.insert("insert", f"开始下载图片...\n")
    for img in imgs:
        # save_img(img)
        pass
    t.insert("insert", f"下载完毕\n")


def save_img(img):
    #t.insert("insert", f"下载中\n")
    # 拼接URL

    img = img if img.find('http') == 0 else "http:"+img
    try:
        response = requests.get(img, headers=headers)
        ctx = response.content
        with open(f'./{time.time()}.jpg', 'wb') as f:
            f.write(ctx)
    except Exception as e:
        print(e.args)


## 5、布局，几行几列， padding内边距， columnspan：跨几列
# 布局有 grid, place, pack
lb.grid(row=1, column=0, padx=10, pady=20)
entry.grid(row=1, column=1, pady=20)
btn.grid(row=1, column=2, padx=10, pady=20)
t.grid(row=2, column=0, padx=20, columnspan=3)


## 6、修改左上角的软件图标，这个地方一般用 .ico 图标
# win.iconbitmap('./icon.ico')


## 进入消息循环，可以写控件（显示窗口）
win.mainloop()
