'''
本案例解决 猫眼影视 里的字体反爬（自定义字体的破解，一般在网页源码中会有 .ttf ）
https://piaofang.maoyan.com/?ver=normal
但是，在编写此案例时，猫眼影视 里的字体是正常的，没有设置反爬
所以，此案例只是跟着案例走了一遍（掌握方法）

'''

import base64

# 看源码，字体为 woff格式
font_face = "d09GRgABAAAAAAggAAsAAAAAC7gAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABHU1VCAAABCAAAADMAAABCsP6z7U9TLzIAAAE8AAAARAAAAF" \
            "ZW7laVY21hcAAAAYAAAAC8AAACTA/VLRxnbHlmAAACPAAAA5EAAAQ0l9+jTWhlYWQAAAXQAAAALwAAADYUwblKaGhlYQAABgAAAAAcAAAA" \
            "JAeKAzlobXR4AAAGHAAAABIAAAAwGhwAAGxvY2EAAAYwAAAAGgAAABoF2gTmbWF4cAAABkwAAAAfAAAAIAEZADxuYW1lAAAGbAAAAVcAA" \
            "AKFkAhoC3Bvc3QAAAfEAAAAXAAAAI/gSKzLeJxjYGRgYOBikGPQYWB0cfMJYeBgYGGAAJAMY05meiJQDMoDyrGAaQ4gZoOIAgCKIwNPAH" \
            "icY2Bk0mWcwMDKwMHUyXSGgYGhH0IzvmYwYuRgYGBiYGVmwAoC0lxTGBwYKr7LMev812GIYdZhuAIUZgTJAQDZjgsneJzFkj0OgzAMhV" \
            "8KpT906NiJE3ThUIgrsLL0BD1Fxk5dOAC3iEgkJEYWRvoSs1SCtXX0RbId+Vl2AOwBROROYkC9oeDtxagK8QjnEI/xoH/DlZEjKpMb3" \
            "Vnbuto1fTkUo56yeeaL7cyaKVZcOz6TUOlE9R0O7DOlqu8w2aj0A1P/k/62S7ifi5eSaoEtmlzg/GC04HfcWYEzhW0Fv1tXC5wzXC" \
            "Nw4uhLwf+RoRC81qgF7gNTJiD+ANtoRPR4nEWTz2/aZhzG39dUOCWEkGHjQlrAmNgGkuDY2ARwDMWBNj8ZCRBCWhqiltJsbbOo6dI2" \
            "2lr2Q2qn/QHdZdIOu1Q79N5J03raOrU59A+o1Otum9RLRPbaIZkPr/S+0vs+n+f7PAYQgMO/gQgIgAGQkEjCR/AAfdBcDrGXwAWAS6" \
            "ZJhwW34owGE0oCLTG4z+jTksvTtwaHnP60L0tjtyr5UPPeg2z9k0hL3b2dvMSiJzDznQPsL2ADAwDQMi1DaUgiGZIbskC9+ycsXGw2a+" \
            "+eleB+Vyg9O0Bnvx7dO/wXA9gbwIAYIvNBSUS6GpyCcc6KW5kgK8cVSfRBknBAJsixHIyzTNBKEpRbVL7rV4VImnNYceiJjSZW73+5Mb2" \
            "jpu8WK3HFBttLk+lqOHKv+Isqj2iyVxnuO2WNeL0PN29+M/d958lPlfFYBabnVxuLhXB05f957CAeO3LBDDkgLpuTkOBOLdDmZyaH+f4kJ" \
            "vhUZyUoegTq6A7ycAr7Hfh7DhQTEedcNEnjGjpwk4ThBdF/a5tRsrWqHtWJ5Ty82n3PBaaZxqNk/vONKa3vZT638bTK+m1wq/ybm3p" \
            "0ff3iijJZP+b6gLhCAIyQdDyhWQysYyUNGhpWHPGiBOGHLtdvG+aTbKpIhufUzDysn959vUtHCV3gReqjvnLZ7/PEYnJAmD03eW" \
            "1mtmBr3diujC2IVIanx85QAz1f/6BuvAHRE18cksMTlKjIPWElgdKhfBBpGxkZgXGdwQuKVuHCqjdkcyRXM4o0bas5k6lySp" \
            "yQxYnMhcftK3un/5jLVfc43rYA01NCRssN1mMT3jO19Tn34KXC5a+26uC4H7CLGAJgFCGxJoDhk+zN1WgF6oiJ4aYgYXIiuqAV/" \
            "mAnQ/FIIELZBwJr0spe6mru1pN5/bOKItu7T7k8q5SKd8uYO06NUP7kuWVlYrzT0u9M/fhiv7EkjJe7r0Yr0frCzEoVWE56Sq" \
            "CUx9C/YvTSzNW0jaJF+wThlkQjk6DVQrgptFGOds8/3XqxvZnLd96ezxaEXFxgaL11/mxwJBgOSGS4/EUJfs1vfnzj9nybd1/JX" \
            "d7T1Gah8XM8E/A39Gz3MZcnXCTBPVwqnczkoMcCXKgL0DTfa4DRM0QiKk6ORbOKeLztxe30WafT7hi+VryuFuql+8sR/kFoDDY7" \
            "s4vltUhWvZlpcYvLs7VXz+/swPV0SsqB/wAGjODCAAAAeJxjYGRgYADixSuWzY3nt/nKwM3CAAI3LlqdRND/37AwMJ0HcjkYmECiAGAm" \
            "DGEAeJxjYGRgYNb5r8MQw8IAAkCSkQEV8AAAM2IBzXicY2EAghQGBiYd4jAAN4wCNQAAAAAAAAAMADAATACUAK4A4AEaAVwBoAHmAhoA" \
            "AHicY2BkYGDgYTBgYGYAASYg5gJCBob/YD4DAA6DAVYAeJxlkbtuwkAURMc88gApQomUJoq0TdIQzEOpUDokKCNR0BuzBiO/tF6QS" \
            "JcPyHflE9Klyyekz2CuG8cr7547M3d9JQO4xjccnJ57vid2cMHqxDWc40G4Tv1JuEF+Fm6ijRfhM+oz4Ra6eBVu4wZvvMFpXLIa40PY" \
            "QQefwjVc4Uu4Tv1HuEH+FW7i1mkKn6Hj3Am3sHC6wm08Ou8tpSZGe1av1PKggjSxPd8zJtSGTuinyVGa6/Uu8kxZludCmzxMEzV0B6U" \
            "004k25W35fj2yNlCBSWM1paujKFWZSbfat+7G2mzc7weiu34aczzFNYGBhgfLfcV6iQP3ACkSaj349AxXSN9IT0j16JepOb01doiKbN" \
            "Wt1ovippz6sVYYwsXgX2rGVFIkq7Pl2PNrI6qW6eOshj0xaSq9mpNEZIWs8LZUfOouNkVXxp/d5woqebeYIf4D2J1ywQB4nG2KOxKAI" \
            "BBDN/hBEe8ioKAlKt7Fxs4Zj++4tKZ5k7yQoBxF/9EQKFCiQg2JBi0UOmj0hEfe15nG2TCHGD8ewSTuwYe8u+zHdWdv8y/Z5JhuW5jRT0QvGVQXkQ=="

print(len(font_face))

## 1、解码，保存为 ttf 文件

b = base64.b64decode(font_face)
with open('font.ttf', 'wb') as f:
    f.write(b)

## 2、处理 ttf 文件，有3种方式：
# 第一种使用软件 FontCreator可以直接打开ttf文件
# 第二种使用 python 的第三方库 fontTools
# 第三种使用百度的 fontstore, http://fontstore.baidu.com/static/editor/index.html

from fontTools.ttLib import TTFont
import re
import requests
import chardet

### 本地已经下载好的字体处理
base_font = TTFont('font.ttf')  # 打开本地的ttf文件

# font.saveXML('01.xml')  # 转为xml文件

base_uni_list = base_font.getGlyphOrder()[2:]   # 获取所有编码，去除前2个，可查看前文图示

# 写出第一次字体文件的编码和对应字体 (查看 01.xml 文件得出)
origin_dict = {'uniE481': '7', 'uniE0AA': '4', 'uniF71E': '9', 'uniE767': '1', 'uniE031': '5', 'uniE4BD': '2','uniF2AA': '3', 'uniE2E3': '6', 'uniE3C9': '8', 'uniEA65': '0'}

### 获取刷新之后在线的字体

url = 'https://piaofang.maoyan.com/?ver=normal'
headers = {
    'User-Agent': '浏览器UA',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
response = requests.get(url=url, headers=headers).content  # 得到字节
# chardet.detect() 函数接受一个参数，一个非unicode字符串， 它返回一个字典， 其中包含自动检测到的字符编码和从0到1的可信度级别。
charset = chardet.detect(response).get('encoding')  # 得到编码格式, {'confidence': 0.98999999999999999, 'encoding': 'GB2312'}
# bytes.decode(encoding=, errors=), 该函数返回字符串。换句话说是bytes类型转化成str类型的函数
# encoding规定解码方式。bytes数据是由什么编码方式编码的，该函数encoding参数就必须用相应解码方式，这样才能返回正确字符串
response = response.decode(charset, "ignore")  # 解码得到字符串

# 获取字体文件的base64编码（查看网页源码知道内容是经过 base64 编码过的，所以要解码）
online_ttf_base64 = re.findall(r"base64,(.*)\) format", response)[0]
online_base64_info = base64.b64decode(online_ttf_base64)
with open('online_font.ttf', 'wb')as f:
    f.write(online_base64_info)
online_font = TTFont('online_font.ttf')  # 网上动态下载的字体文件。

online_uni_list = online_font.getGlyphOrder()[2:]


for uni2 in online_uni_list:
    obj2 = online_font['glyf'][uni2]  # 获取编码uni2在online_font.ttf中对应的对象
    for uni1 in base_uni_list:
        obj1 = base_font['glyf'][uni1]  # 获取编码uni1在base_font.ttf 中对应的对象
        if obj1 == obj2:  # 判断两个对象是否相等
            dd = "&#x" + uni2[3:].lower() + ';'  # 修改为Unicode编码格式
            if dd in response:  # 如果编码uni2的Unicode编码格式 在response中，替换成origin_dict中的数字。
                response = response.replace(dd, origin_dict[uni1])



