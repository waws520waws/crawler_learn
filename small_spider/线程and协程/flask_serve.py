
'''
Flask 是一个使用 Python 语言编写的 Web 框架，它可以让你高效的编写 Web 程序。Web 程序即“网站”或“网页程序”，是指可以通过浏览器进行交互的程序。
我们日常使用浏览器访问的豆瓣、知乎、百度等网站都是 Web 程序。

下面的程序在运行后，可以在浏览器上访问这些路径
'''

from flask import Flask
import time

app = Flask(__name__)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return "Hello jay"

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'

if __name__ == '__main__':
    app.run(threaded=True)