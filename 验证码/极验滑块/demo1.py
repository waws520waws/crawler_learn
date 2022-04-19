'''
分析步骤见 demo1.md
'''
import time
from PIL import Image
import io
import execjs
import random
import requests


def get_standard_img(content: bytes):
    '''
    实现部分参考：https://github.com/nmsdss/JiYan_Geetest
    :param content: 二进制图片
    :return: 还原后的图片对象
    '''

    # 乱码图每个小块的正确位置
    Ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12,
          13,
          23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]

    r = 160
    a = r // 2

    # 使用io.BytesIO()可以解决读取时的编码问题
    image = Image.open(io.BytesIO(content))
    standard_img = Image.new("RGBA", (260, 160))
    for _ in range(52):
        c = Ut[_] % 26 * 12 + 1
        u = a if 25 < Ut[_] else 0
        l = image.crop(box=(c, u, c + 10, u + a))  # 截图
        ## 参数必须是int型，所以上面的 a=r//2
        standard_img.paste(l, box=(_ % 26 * 10, a if 25 < _ else 0))  # 一张图片（l）粘贴到另一张图片(standard_img)上去

    standard_img.save('./full_picture/full1.png')
    return standard_img


def get_distance(gap_bg_obj: object, full_bg_obj: object) -> int:
    """
      拿到滑动验证码需要移动的距离
      :param gap_bg_obj:带缺口的图片对象
      :param full_bg_obj:没有缺口的图片对象
      :return:需要移动的距离
    """

    threshold = 50
    for i in range(0, gap_bg_obj.size[0]):  # 260
        for j in range(0, gap_bg_obj.size[1]):  # 160
            pixel1 = gap_bg_obj.getpixel((i, j))
            pixel2 = full_bg_obj.getpixel((i, j))
            res_R = abs(pixel1[0] - pixel2[0])  # 计算RGB差
            res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
            res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
            if res_R > threshold and res_G > threshold and res_B > threshold:
                return i - 5


def get_track(distance: int) -> list:
    '''
    模拟真实轨迹
    :param distance: 原始路径（非差值）
    :return:
    '''
    track = [[random.randint(-20, -40), random.randint(-20, -40), 0]]
    track.append([0, 0, 0])
    track_time = random.randint(100, 200)
    track.append([1, 0, track_time])

    x = 1
    count = 0
    scale = [0.2, 0.5, random.randint(6, 8) / 10]
    while count < distance:
        if count < distance * scale[0]:
            x += random.randint(1, 2)
            track_time += random.randint(10, 20)
        elif count < distance * scale[1]:
            x += random.randint(3, 4)
            track_time += random.randint(10, 20)
        elif count < distance * scale[2]:
            x += random.randint(5, 6)
            track_time += random.randint(50, 100)
        elif count < distance * 0.9:
            x += random.randint(2, 3)
            track_time += random.randint(200, 300)
        elif count < distance:
            x += 1
            track_time += random.randint(10, 20)
        count += x
        track.append([
            x,
            random.choice([0, 0, 0, 0, 0, 0, -1, 1]),
            track_time
        ])
    return track


def get_aa():
    # 得自己生成一个轨迹（正常拖动滑块应该是由慢到快再到慢，所以时间应该是先增大再减小）
    track = [[-27, -21, 0], [0, 0, 0], [1, 0, 39], [2, 0, 65], [4, 0, 79], [5, 0, 87], [6, -1, 95], [7, -1, 112],
             [8, -1, 119], [10, -1, 128], [11, -1, 140], [13, -1, 144], [15, -1, 152], [17, -1, 160], [19, -1, 175],
             [21, -1, 183], [22, -1, 191], [23, -1, 200], [24, -1, 215], [25, -1, 232], [25, -1, 319]]

    arr_c = [12, 58, 98, 36, 43, 95, 62, 15, 12]
    s = "6a48365a"

    aa = docjs.call('get_aa', track, arr_c, s)
    print('aa: ', aa)
    return aa


def get_rp():
    passtime = 319  # 通过时间，为轨迹中的最后时间
    gt = "019924a82c70bb123aae90d483087f94"
    challenge = "174a6ead4600caa62f4ea0fa4dd906c5c7"

    rp = docjs.call('getRp', gt+challenge[:32]+str(passtime))
    print('rp: ', rp)
    return rp


def get_userresponse():
    max_x = 25  # 最大x的坐标
    userresponse = docjs.call('getUserresponse', max_x, challenge)
    print('userresponse: ', userresponse)
    return userresponse


def get_w():
    aa = get_aa()
    rp = get_rp()
    userresponse = get_userresponse()
    passtime = 319  # 通过时间，为轨迹中的最后时间
    result_u = docjs.call('get_u')
    result_l = docjs.call('get_l', aa, rp, userresponse, passtime)
    result_h = docjs.call('get_h', result_l)
    result_w = result_h + result_u
    return result_w


with open('./slide.7.8.6.js', 'r', encoding='utf-8') as f:
    js = f.read()

docjs = execjs.compile(js)
get_w()

session = requests.session()

def get_challenge_gt():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    try:
        params = {
            't': int(time.time() * 1000)
        }
        url_register = 'https://www.geetest.com/demo/gt/register-slide'
        res = session.get(url_register, params=params, headers=headers)
        challenge = res.json()['challenge']
        gt = res.json()['gt']
        return challenge, gt
    except Exception as e:
        raise e

def get_c_s():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    try:
        gt, challenge = get_challenge_gt()
        params = {
            'gt': gt,
            'challenge': challenge,
            'w': w
        }
        url_get = 'https://apiv6.geetest.com/get.php'
        session.get(url_get, headers=headers, params=params)

    except Exception as e:
        raise e

def main():
