#from tkinter import Tk
import tkinter as tk
import requests
import re
import time
# 创建主窗口
win = tk.Tk()
# 设置标题
win.title("抓图小程序")

# 窗体大小设置
width = 500
height = 400
# 获取屏幕分辨率
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
position = f"{width}x{height}+{(screen_width-width)/2:.0f}+{(screen_height-height)/2:.0f}"
win.geometry(position)
# win.geometry('500x300+200+400')
# 进入消息循环，可以写控件

# 通用页面headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    "Referer":"https://img3.chinadaily.com.cn"
}

# 创建提示文本
lb = tk.Label(win, text='请输入网址：')
# 创建文本框
entry = tk.Entry(win,width=30) # width 设置输入框的宽度，以字符为单位，默认值是20
# 创建一个多行文本框
t = tk.Text(win, width=60,height=20)

# 下载图片
def save_img(img):
    #t.insert("insert", f"下载中\n")
    # 拼接URL

    img = img if img.find('http')==0 else "http:"+img
    try:
        response = requests.get(img,headers=headers)
        ctx = response.content
        with open(f'./{time.time()}.jpg', 'wb') as f:
            f.write(ctx)
    except Exception as e:
        print(e.args)

# 分析网页图片清单
def analyse(url):
    resp = requests.get(url,headers=headers)
    content = resp.text # 获取到网页内容
    #print(content)
    imgs = re.findall('img src="(.*?)"', content)
    # 界面展示获取到的图片数量

    t.insert("insert", f"获取到{len(imgs)}张图片\n")
    t.insert("insert", f"开始下载图片...\n")
    for img in imgs:
        save_img(img)
    t.insert("insert", f"下载完毕\n")



# 事件函数
def down_img():
    # print("hello world")
    # 获取文本框内容
    url = entry.get()
    analyse(url)

# 创建按钮
btn = tk.Button(win,text = '分析下载', command = down_img)


lb.grid(row=1,column=0,padx=10,pady=20)
entry.grid(row=1,column=1,pady=20)
btn.grid(row=1,column=2,padx=10,pady=20)
t.grid(row=2,column=0,padx=20,columnspan=3)

win.mainloop()
