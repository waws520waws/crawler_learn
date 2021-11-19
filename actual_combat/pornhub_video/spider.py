import re


'''
需求：爬取 pornhub.com 中的视频
在请求后的网页源码中，script标签下的js代码中，可以找出拼接出视频地址的代码
'''

## 1 这段字符串代码可以在网页源码中正则匹配出来 【注意匹配的范围与下面字符串的范围一致，否则要改代码】
string1 = 'var rajnja5ra39rajnja5ra39="jNjA5";var ratpra72ratpra72="t=p";var rae0366ra92rae0366ra92="e0366";var ramzczmra79ramzczmra79="MzczM";var rammqymra73rammqymra73="MmQyM";var radeogra48radeogra48="deo/g";var rajmzyjra95rajmzyjra95="jMzYj";var raisinqra74raisinqra74="IsInQ";var ra078b2ra16ra078b2ra16="078b2";var rawu3yira71rawu3yira71="WU3Yi";var rag3yjlra67rag3yjlra67="g3Yjl";var rayjawmra66rayjawmra66="YjAwM";var rahttpsra77rahttpsra77="https";var rad9vra32rad9vra32="d9&v=";var ra4ytnkra79ra4ytnkra79="4YTNk";var rati2mzra61rati2mzra61="TI2Mz";var rae4njyra32rae4njyra32="E4NjY";var ramm2yjra62ramm2yjra62="mM2Yj";var radflowra29radflowra29="DFlOW";var rahmwy2ra73rahmwy2ra73="hMWY2";var rapornra17rapornra17=".porn";var raijoizra66raijoizra66="IjoiZ";var raioje2ra6raioje2ra6="iOjE2";var radiasra61radiasra61="dia?s";var rae0ra46rae0ra46="&e=0&";var racnra38racnra38="://cn";var raeyjrra49raeyjrra49="=eyJr";var raph616ra44raph616ra44="ph616";var raq5mwmra31raq5mwmra31="Q5MWM";var rahubcra83rahubcra83="hub.c";var raetmera20raetmera20="et_me";var rajrjowra45rajrjowra45="jRjOW";var razmotlra97razmotlra97="ZmOTl";var razdu5nra71razdu5nra71="ZDU5N";var raomvira30raomvira30="om/vi";var rangi2mra64rangi2mra64="NGI2M";var rawmdbmra23rawmdbmra23="wMDBm";var media_5=/* + ra4ytnkra79ra4ytnkra79 + */rahttpsra77rahttpsra77 + /* + ra4ytnkra79ra4ytnkra79 + */racnra38racnra38 + /* + ramm2yjra62ramm2yjra62 + */rapornra17rapornra17 + /* + radeogra48radeogra48 + */rahubcra83rahubcra83 + /* + radiasra61radiasra61 + */raomvira30raomvira30 + /* + rawmdbmra23rawmdbmra23 + */radeogra48radeogra48 + /* + raioje2ra6raioje2ra6 + */raetmera20raetmera20 + /* + rahmwy2ra73rahmwy2ra73 + */radiasra61radiasra61 + /* + rahttpsra77rahttpsra77 + */raeyjrra49raeyjrra49 + /* + rajnja5ra39rajnja5ra39 + */raijoizra66raijoizra66 + /* + radeogra48radeogra48 + */rajrjowra45rajrjowra45 + /* + radiasra61radiasra61 + */raq5mwmra31raq5mwmra31 + /* + rae0366ra92rae0366ra92 + */rawmdbmra23rawmdbmra23 + /* + ratpra72ratpra72 + */rangi2mra64rangi2mra64 + /* + rag3yjlra67rag3yjlra67 + */rajmzyjra95rajmzyjra95 + /* + rati2mzra61rati2mzra61 + */razmotlra97razmotlra97 + /* + raomvira30raomvira30 + */rajnja5ra39rajnja5ra39 + /* + raetmera20raetmera20 + */razdu5nra71razdu5nra71 + /* + raetmera20raetmera20 + */ramm2yjra62ramm2yjra62 + /* + rangi2mra64rangi2mra64 + */rag3yjlra67rag3yjlra67 + /* + rahubcra83rahubcra83 + */rahmwy2ra73rahmwy2ra73 + /* + rangi2mra64rangi2mra64 + */rammqymra73rammqymra73 + /* + rawu3yira71rawu3yira71 + */radflowra29radflowra29 + /* + raisinqra74raisinqra74 + */rae4njyra32rae4njyra32 + /* + radflowra29radflowra29 + */ra4ytnkra79ra4ytnkra79 + /* + radeogra48radeogra48 + */rayjawmra66rayjawmra66 + /* + rapornra17rapornra17 + */rawu3yira71rawu3yira71 + /* + rajmzyjra95rajmzyjra95 + */raisinqra74raisinqra74 + /* + raijoizra66raijoizra66 + */raioje2ra6raioje2ra6 + /* + raisinqra74raisinqra74 + */ramzczmra79ramzczmra79 + /* + ratpra72ratpra72 + */rati2mzra61rati2mzra61 + /* + razmotlra97razmotlra97 + */rad9vra32rad9vra32 + /* + rahttpsra77rahttpsra77 + */raph616ra44raph616ra44 + /* + ra4ytnkra79ra4ytnkra79 + */rae0366ra92rae0366ra92 + /* + rangi2mra64rangi2mra64 + */ra078b2ra16ra078b2ra16 + /* + raisinqra74raisinqra74 + */rae0ra46rae0ra46 + /* + raioje2ra6raioje2ra6 + */ratpra72ratpra72;'

## 2 下面就是根据上面的字符串中的规则拼接出视频地址
##【注意】地址有时效性

s1, s2 = string1.split('var media_5=')

s1 = s1.replace('var ', '')
s1 = s1.replace('"', '')
s1 = s1.split(';')
dic_d = {}
# print(len(s1))
for s in s1:
    if s:
        k, v = s.split('=', maxsplit=1)
        dic_d[k] = v

# print(dic_d)
# print(len(dic_d))


s2 = re.sub('/\*.*?\*/', '', s2)   # 正则替换
s2 = s2.replace(';', '')
s2 = s2.split(' + ')
# print(s2)

media_5 = ''
print(dic_d)
for k in s2:
    # print(dic_d[k])
    v = dic_d[k].split(' + ')
    v = ''.join(v)
    media_5 += v

print(media_5)

## 3 请求上面得到的地址，返回mp4地址