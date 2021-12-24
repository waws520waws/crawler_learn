from fontTools.ttLib import TTFont

### 本地已经下载好的字体处理
base_font = TTFont('Python爬虫100例教程/7反爬-63-字体反爬1(猫眼影视)/font.ttf')  # 打开本地的ttf文件

# font.saveXML('01.xml')  # 转为xml文件

base_uni_list = base_font.getGlyphOrder()[2:]   # 获取所有编码，去除前2个，可查看前文图示

print(base_uni_list)

obj1 = base_font['glyf']['uniE481']

print(obj1)