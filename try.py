from PIL import Image

a = Image.new('RGB', (300, 300), (255, 0, 0))  # 生成一张300*300的红色图片
b = Image.new('RGB', (200, 200), (0, 255, 0))  # 200*200的绿色图片
a.paste(b, (50, 50, 250, 250))  # 将b贴到a的坐标为（100，100）的位置
a.show()  # 显示a