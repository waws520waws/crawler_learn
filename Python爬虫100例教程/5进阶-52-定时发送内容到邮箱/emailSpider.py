import re
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

import requests


class SendEmail():

    # 初始化数据
    def __init__(self):
        self.start_url = "https://www.cnblogs.com/cate/python"
        self.headers = {
            "user-agent": "Mozilla/..... Safari/537.36",
            "referer": "https://www.cnblogs.com/cate/python/"
        }
        self.pattern = r'<div class="post_item_body">[\s\S.]*?<h3><a class="titlelnk" href="(.*?)" target="_blank">(.*?)</a></h3>[\s\S.]*?<div class="post_item_foot">[\s\S.]*?<a href=".*?" class="lightblue">(.*?)</a>([\s\S.]*?)<span class="article_comment">'
        self.last_blog_time = 0
        self.need_send_articles = []

    # 解析网页内容
    def get_articles(self):
        try:
            # 正常的数据获取
            res = requests.get(self.start_url, headers=self.headers, timeout=3)
        except Exception as e:
            print("error %s" % e)
            time.sleep(3)
            return self.get_articles()  # 重新发起请求

        html = res.text
        # 这个地方的正则表达式是考验你正则功底的地方了
        all = re.findall(self.pattern, html)
        # 判断，如果没有新文章
        last_time = self.change_time(all[0][3].strip().replace("发布于 ", ""))

        if last_time <= self.last_blog_time:
            print("没有新文章更新")
            return

        for item in all:
            public_time = item[3]
            if public_time:
                # 格式化时间
                public_time = self.change_time(public_time.strip().replace("发布于 ", ""))

                if (public_time > self.last_blog_time):
                    self.need_send_articles.append({
                        "url": item[0],
                        "title": item[1],
                        "author": item[2],
                        "time": public_time
                    })

        # 文章获取完毕，更新时间
        self.last_blog_time = last_time
        ##### 测试输出
        print(self.need_send_articles)
        print("现在文章的最后时间为", self.last_blog_time)
        ##### 测试输出
        self.send_email(self.need_send_articles)

    def change_time(self, need_change_time):
        '''
        # 时间的转换
        :param need_change_time:
        :return:返回时间戳
        '''
        time_array = time.strptime(need_change_time, "%Y-%m-%d %H:%M")
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    # 发送邮件
    def send_email(self, articles):
        '''
        并未实现定时
        '''
        smtp = smtplib.SMTP_SSL()  # 这个地方注意
        smtp.connect("smtp.qq.com", 465)  # QQ邮箱 SMTP 服务器地址及端口号
        smtp.login("1410203345@qq.com", "授权码")  # QQ邮箱 -》设置 -》账户 -》开启服务，可获取到授权码

        sender = '1410203345@qq.com'
        receivers = ['找个自己的其他邮箱@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 完善发件人收件人，主题信息
        message = MIMEMultipart()
        message['From'] = formataddr(["博客采集器", sender])
        message['To'] = formataddr(["hi,baby", ''.join(receivers)])
        subject = '你有新采集到的文章清单'
        message['Subject'] = Header(subject, 'utf-8')
        # 正文部分
        html = ""
        for item in articles:
            html += ("<p><a href='{url}'>{title}</a>--文章作者{author}--发布时间{time}</p>".format(title=item["title"],
                                                                                           url=item["url"],
                                                                                           author=item["author"],
                                                                                           time=item["time"]))

        textmessage = MIMEText('<p>新采集到的文章清单</p>' + html,
                               'html', 'utf-8')
        message.attach(textmessage)

        # 发送邮件操作
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()


s = SendEmail()
s.get_articles()
