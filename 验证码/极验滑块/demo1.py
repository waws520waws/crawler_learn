'''
分析步骤见 demo1.md
'''
import time
from PIL import Image
import io
import execjs
import random
import requests
import json
import re

session = requests.session()


def get_standard_img(content: bytes):
    '''
    实现部分参考：https://github.com/nmsdss/JiYan_Geetest
    :param content: 二进制图片
    :return: 还原后的图片对象
    '''

    # 乱码图每个小块的正确位置
    Ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12,
          13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]

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
    track = [[-random.randint(20, 40), -random.randint(20, 40), 0]]
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
    return track, track_time


def get_aa(docjs, gap_bg_url, full_bg_url, arr_c, s):
    # 请求得到乱码图片
    try:
        domain = 'https://static.geetest.com/'
        response1 = requests.get(domain + gap_bg_url)
        response2 = requests.get(domain + full_bg_url)

        gap_bg = response1.content
        full_bg = response2.content

    except Exception as e:
        raise e

    # 图片还原
    standard_gap_bg = get_standard_img(gap_bg)
    standard_full_bg = get_standard_img(full_bg)

    # 得到滑动轨迹
    distance = get_distance(standard_gap_bg, standard_full_bg)
    track, track_time = get_track(distance)

    aa = docjs.call('get_aa', track, arr_c, s)
    print('aa: ', aa)
    return aa, track_time


def get_rp(docjs, gt, challenge, passtime):
    # passtime = 319  # 通过时间，为轨迹中的最后时间

    rp = docjs.call('getRp', gt + challenge[:32] + str(passtime))
    print('rp: ', rp)
    return rp


def get_userresponse(docjs, gt, challenge):
    max_x = 25  # 最大x的坐标
    userresponse = docjs.call('getUserresponse', max_x, challenge)
    print('userresponse: ', userresponse)
    return userresponse


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
        return gt, challenge
    except Exception as e:
        raise e


def get_fullpage_w(gt, challenge):
    with open('./fullpage.9.0.9.js', 'r', encoding='utf-8') as f:
        js1 = f.read()

    fullpage_js = execjs.compile(js1)
    fullpage_w = fullpage_js.call('get_fullpage_w', gt, challenge)
    return fullpage_w


def get_c_s(gt, challenge):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'apiv6.geetest.com',
        'Referer': 'https://www.geetest.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    try:
        params = {
            'gt': gt,
            'challenge': challenge,
            'lang': "zh-cn",
            'pt': 0,
            'client_type': 'web',
            # 'w': get_fullpage_w(gt, challenge),  # 这里不要w参数反而请求成功了，为啥？
            # 'callback': 'geetest_' + str(int(time.time() * 1000))  # 加这个参数也要出错
        }
        url_get = 'https://apiv6.geetest.com/get.php'
        res = session.get(url_get, headers=headers, params=params)
        print('get_c_s: ', res.text)
        response_dict = res.text[1:-1]
        response_dict = json.loads(response_dict)
        return None

    except Exception as e:
        raise e


def get_ajax_w(gt, challenge, gap_bg_url, full_bg_url, c, s):
    with open('./slide.7.8.6.js', 'r', encoding='utf-8') as f:
        js = f.read()

    docjs = execjs.compile(js)

    aa, passtime = get_aa(docjs, gap_bg_url, full_bg_url, c, s)
    rp = get_rp(docjs, gt, challenge, passtime)
    userresponse = get_userresponse(docjs, gt, challenge)
    # passtime = 319  # 通过时间，为轨迹中的最后时间
    result_u = docjs.call('get_u')
    result_l = docjs.call('get_l', aa, rp, userresponse, passtime)
    result_h = docjs.call('get_h', result_l)
    ajax_w = result_h + result_u
    return ajax_w


def get_material(gt, challenge):
    '''
    获取所需素材
    :param gt: old gt
    :param challenge: old challenge
    :return: 新的gt、新的challenge、图片
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    try:
        params = {
            "is_next": "true",
            "type": "slide3",
            "gt": gt,
            "challenge": challenge,
            "lang": "zh-cn",
            "https": "true",
            "protocol": "https://",
            "offline": "false",
            "product": "embed",
            "api_server": "api.geetest.com",
            "isPC": "true",
            "autoReset": "true",
            "width": "100%",
        }
        url_slide_get = 'https://api.geetest.com/get.php'
        response = session.get(url_slide_get, params=params)
        print('get_material: ', response.text)
        data = re.search(r"new Geetest\((.*?),true\)", response.text).group(1)
        data_dict = eval(data.replace("true", "'true'").replace("false", "'false'"))
        gt = data_dict["gt"]
        s = data_dict["s"]
        c = data_dict["c"]
        challenge = data_dict["challenge"]
        id = data_dict["id"]
        gap_bg = data_dict["bg"]  # 带缺口的背景
        full_bg = data_dict["fullbg"]  # 不带缺口的背景
        # slice = data_dict["slice"]  # 缺口小图
        gct_path = data_dict["gct_path"][1:]  # gct.js的地址
        return gt, challenge, c, s, id, gap_bg, full_bg, gct_path

    except Exception as e:
        raise e


def first_ajax_req(gt, challenge):
    '''
    点击按钮后会第一次请求一个 ajax.php 链接，应该是获取验证方式
    :param gt:
    :param challenge:
    :return:
    '''
    try:
        params = {
            "gt": gt,
            "challenge": challenge,
            "lang": "zh-cn",
            "pt": 0,
            "client_type": "web",
            "w": "",  # w值可置空, 留作扩展
        }
        url_ajax = 'https://api.geetest.com/ajax.php'
        response = session.get(url_ajax, params=params)
        response_dict = response.text[1:-1]
        response_dict = json.loads(response_dict)
        print(f"获取验证方式成功 -> {response.status_code, response_dict}")
    except Exception as e:
        raise e

def validate(gt, challenge, w):
    '''
    最后的验证
    :param gt:
    :param challenge:
    :param w:
    :return:
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    try:
        print(gt)
        print(challenge)
        print('ajax w: ', w)
        params = {
            "gt": gt,
            "challenge": challenge,
            "lang": "zh-cn",
            "$_BBF": 0,
            "client_type": "web",
            "w": w,
        }
        url_ajax = 'https://api.geetest.com/ajax.php'
        response = session.get(url_ajax, headers=headers, params=params)
        print('validate: ', response.text)
        response_dict = response.text[1:-1]
        response_dict = json.loads(response_dict)

        if response_dict["message"] == "success":
            print(f"验证通过 -> {response.status_code, response_dict}")
            return response_dict["validate"]
        elif response_dict["message"] == "fail":
            print(f"验证不通过,未能正确拼合图像 -> {response.status_code, response_dict}")
            return None
        elif response_dict["message"] == "forbidden":
            print(f"轨迹验证不通过 -> {response.status_code, response_dict}")
            return None

    except Exception as e:
        raise e


def main():
    gt, challenge = get_challenge_gt()
    get_c_s(gt, challenge)
    first_ajax_req(gt, challenge)
    new_gt, new_challenge, c, s, id, gap_bg_url, full_bg_url, gct_path = get_material(gt, challenge)
    ajax_w = get_ajax_w(new_gt, new_challenge, gap_bg_url, full_bg_url, c, s)
    validate1 = validate(new_gt, new_challenge, ajax_w)
    print('validate: ', validate1)


if __name__ == '__main__':
    main()
