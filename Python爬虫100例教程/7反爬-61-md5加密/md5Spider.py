import requests
import hashlib
import time
import random


def md5_enc(e):
    # 【md5一旦加密，数据就不能返回成原来的值了，是不可以解密的】
    ## ====================== bv
    ua = '5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

    # 1、创建hash对象
    hl = hashlib.md5()

    # 2、向hash对象中添加需要做hash运算的字符串
    hl.update(ua.encode('utf-8'))  # 这个地方传的是bytes类型的数据，否则会报错

    # 3、获取字符串的hash值
    bv = hl.hexdigest()


    ### 或者只需要一句代码
    # str1_md5 = hashlib.md5(str1.encode(encoding='utf-8')).hexdigest()

    ## ====================== ts
    t = time.time()
    ts = str(round(t * 1000))

    ## ====================== salt
    salt = ts + str(random.randint(0, 9))

    ## ====================== sign
    str1 = "fanyideskweb" + e + salt + "Y2FYu%TNSbMCxc3t2u^XT"
    sign = hashlib.md5(str1.encode('utf-8')).hexdigest()

    return bv, ts, salt, sign


def main():
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    words = 'jay'
    bv, ts, salt, sign = md5_enc(words)

    data = {
        'i': 'jay',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    res = requests.post(url, data=data)

    resdata = res.json()
    print(resdata)


if __name__ == '__main__':
    main()