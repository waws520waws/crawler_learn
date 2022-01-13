'''
newspaper框架都是基于关键字识别的，有一些BUG存在，有时识别不准
'''

from newspaper import Article
import newspaper

## 单个新闻网页爬取
# 只爬取当前url的内容

url = 'https://onezero.medium.com/apple-watch-5f690f4de6c'

article = Article(url, language='zh')  # 创建文章对象
article.download()      # 加载网页 （可以加载本地文件）
article.parse()         # 解析网页
# print(article.html)     # 打印html文档
#
print(article.text)     # 新闻正文
print("-"*100)
print(article.title)    # 新闻标题
print("-"*100)
print(article.authors)  # 新闻作者
print("-"*100)
print(article.summary)   # 新闻摘要
print(article.keywords)  # 新闻关键词
# print(article.top_image)  # 本文的top_image的URL
# print(article.images)     # 本文中的所有图像url


## 同网站下多条新闻url爬取
# 会爬取当前url对应的网页中的所有url

# memoize_articles: 是否记住已经爬过的url（去重，增量式爬虫）
sina_paper = newspaper.build('http://www.lemonde.fr/', language='fr', memoize_articles=False)  # 构建新闻源
sina_paper.size()   # 查看有多少链接

first_article = sina_paper.articles[0]
first_article.download()
first_article.parse()

# 查看新闻源下面的所有新闻链接
for article in sina_paper.articles:
    print(article.url)

# 提取源类别（不同域名的首页url）
for category_url in sina_paper.category_urls():
    print(category_url)



