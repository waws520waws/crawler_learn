'''
参考：https://www.bilibili.com/video/BV1i54y1h75W?p=46
需求：爬取网易云音乐上的热评

难点：请求参数加密、js逆向；编码解码

'''

# pip install pycrypto ,若失败，则 pip install pycryptodome
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

## 1、找到加密数据（通过js逆向找到）
data = {
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_1880849699",
    'threadId': "R_SO_4_1880849699"
}

## 2、处理加密过程（通过js逆向找）
'''
加密代码：
var bKf7Y = window.asrsea(JSON.stringify(i7b), bva4e(["流泪", "强"]), bva4e(Tu9l.md), bva4e(["爱心", "女孩", "惊恐", "大笑"]));
'''
### 2.1 找到加密函数

'''
function a(a) {  # 产生16位随机数（可读代码，也可在浏览器中设置断点查看返回值）
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {  # a是要加密的内容，
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {  ## AES加密，c是密钥（加密需要密钥）
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC  # 用CBC模式加密
        });
        return f.toString()
    }
    function c(a, b, c) {  # c不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  # d: 加密数据，e：010001，f：很长，g：0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);  # i是16位随机数, 可以设置成定值
        return h.encText = b(d, g),  ## g是密钥
        h.encText = b(h.encText, i), 
        h.encSecKey = c(i, e, f),  # 只有i是随机数，i定值的话，那么返回得到的 h.encSecKey 也是定值
        h
    }
'''

### 2.2 通过对上面的加密函数的分析，得出以下信息，并用python实现

#### 2.2.1 通过在浏览器的console执行，发现以下参数是固定值
e = '010001'  # bva4e(["流泪", "强"])
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135' \
    'fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef5274' \
    '1d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'  # bva4e(["爱心", "女孩", "惊恐", "大笑"])

#### 2.2.2 加密函数中的i是16位随机数, 可以设置成定值
# 在浏览器中设置断点查看i的值
i = "NOLr4ipDZ5A9mMSV"


#### 2.2.3 加密函数中产生 h.encSecKey 的过程中只有i是随机数，i定值的话，那么返回得到的 h.encSecKey 也是定值
# 在浏览器中设置断点查看当前i对应的 h.encSecKey
def get_encSecKey():
    return "4b718b4eb0223bcb3d074d7742c505b503a2d60b9c4e4056d3e98078036f07095fc854a536754eaf63fb57b451a39f4bd992d20ac5ab5be0b0eb0e5a7dd7e7b8114c5091dabb427a06292ca686067ec802e09b0ca3fde2edb2ecc179b76a0d16d4ba019f28d0b9881a013b32eb01d7056704b80b1b50d78594a2b529ee632458"


#### 2.2.3 产生 h.encText 使用了两次加密


def get_params(data):  # data为字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):
    iv = '0102030405060708'
    # mode: 模式，先看m3u8文件是否提示用的什么模式，没有的话就一个一个的试
    # IV：偏移量，字节型，位数与key相同
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)  # 创建加密器

    # 加密的内容长度必须是16的倍数【长度刚好是16也是需要加上chr(需要补齐的位数)进行补齐,不够要补，够了也要补】
    # chr()返回值是当前整数对应的 ASCII 字符
    # 如：'123456789abcde'，差1位，则需要1个chr(1)补齐成这样：'123456789abcdechr(1)'
    # 如：'123456789abc'，差4位，则需要4个chr(4)补齐成这样：'123456789abcchr(4)chr(4)chr(4)chr(4)'
    # 如：'123456789abcdef'，刚好16位，则需要16个chr(16)补齐成这样：'123456789abcdefchr(16)。。。chr(16)'
    data = to_16(data)

    # byte类型数据
    data_byte = aes.encrypt(data.encode('utf-8'))  # 加密
    # 加密后的数据无法用decode，解码不出来，因为是加密

    return str(b64encode(data_byte), 'utf-8')


if __name__ == '__main__':
    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    req = requests.post(url, data={
        'params': get_params(json.dumps(data)),  # json型字符串
        'encSecKey': get_encSecKey()
    })
    print(req.text)
