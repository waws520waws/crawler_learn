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
    Ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12, 13,
          23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]

    r = 160
    a = r/2

    image = Image.open(io.BytesIO(content))
    standard_img = Image.new("RGBA", (260, 160))
    for _ in range(52):
        c = Ut[_] % 26 * 12 + 1
        u = a if 25 < Ut[_] else 0
        l = image.crop(box=(c, u, c+10, u+a))
        standard_img.paste(l, box=(c % 26 * 10, 80 if c > 25 else 0))

    return standard_img