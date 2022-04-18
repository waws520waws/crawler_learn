'''
分析步骤见 demo1.md
'''

from PIL import Image
import io


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
        ## 参数必须是init型，所以上面的 a=r//2
        standard_img.paste(l, box=(_ % 26 * 10, a if 25 < _ else 0))  # 一张图片（l）粘贴到另一张图片(standard_img)上去

    standard_img.save('./full_picture/full1.png')
    return standard_img


# with open('luanma_picture/d401d55fc.webp', 'rb') as f:
#     im = f.read()
#
# get_standard_img(im)

'''
u = r[$_CAGEe(750)]()
l = V[$_CAGEe(342)](gt[$_CAGEe(209)](o), r[$_CAGEe(742)]())
h = m[$_CAGEe(733)](l)
'''

import execjs

with open('./slide.7.8.6.js', 'r', encoding='utf-8') as f:
    js = f.read()

docjs = execjs.compile(js)
result = docjs.call('get_u')
# print(result)

'''
实现 `l = n[$_CJJIW(1078)][$_CJJJd(1069)](n[$_CJJIW(1078)][$_CJJJd(1051)](), n[$_CJJJd(13)][$_CJJIW(1045)], n[$_CJJIW(13)][$_CJJIW(307)]);`
'''

## 得自己生成一个轨迹（正常拖动滑块应该是由慢到快再到慢，所以时间应该是先增大再减小）
track = [[-27, -21, 0], [0, 0, 0], [1, 0, 39], [2, 0, 65], [4, 0, 79], [5, 0, 87], [6, -1, 95], [7, -1, 112],
         [8, -1, 119], [10, -1, 128], [11, -1, 140], [13, -1, 144], [15, -1, 152], [17, -1, 160], [19, -1, 175],
         [21, -1, 183], [22, -1, 191], [23, -1, 200], [24, -1, 215], [25, -1, 232], [25, -1, 319]]

arr_c = [12, 58, 98, 36, 43, 95, 62, 15, 12]
s = "6a48365a"

new_track = docjs.call('get_l', track, arr_c, s)
print(new_track)

## 获取rp值
passtime = 319  # 通过时间，为轨迹中的最后时间
gt = "019924a82c70bb123aae90d483087f94"
challenge = "174a6ead4600caa62f4ea0fa4dd906c5c7"

rp = docjs.call('getRp', gt+challenge[:32]+str(passtime))
print(rp)

max_x = 25  # 最大x的坐标
userresponse = docjs.call('getUserresponse', max_x, challenge)
print(userresponse)