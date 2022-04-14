- 【官方文档】https://pillow.readthedocs.io/en/latest/reference/Image.html
- 安装： `pip install pillow`

### Image模块

#### 打开图片

```python
from PIL import Image
im = Image.open("bride.jpg", mode='r')  
im.rotate(45).show()  # 旋转，和显示图像(使用默认的查看器) 
```
#### 新建图像

​	Image.new(mode, size[, color])

​	以指定的模式和大小创建一个新图像。

​		mode：有RGB、RGBA；

​		size：2元元组(width, height)；

​		color：图像以黑色填充

```python
from PIL import Image
im = Image.new("RGBA", (260, 160))
```

#### 图片的裁剪

im.crop(box=(x0,y0,x1,y1))：裁剪

```python
from PIL import Image
image = Image.open("bride.jpg")
image_crop = image.crop(box=(300, 300, 800, 700))
```



#### 粘贴图片

image.paste(im, box=None[, mask=None])

将另一张图片粘贴到当前图片中，如果粘贴的模式不匹配，则将被粘贴图片的模式转换成当前图片的模式.

​	im：粘贴的图片；

​	box：图片粘贴的位置或区域。传入一个长度为2或4的元组，如果不传值，默认为(0, 0)，图片被粘贴在当前图片的左上角。如果传入长度为2的元组(x, y)，表示被粘贴图片的左上角坐标位置。如果传入长度为4的元组(x1, y1, x2, y2)，表示图片粘贴的区域，此时区域的大小必须与粘贴的图片一致，否则会报错，传入的元组长度为其他值也会报错。

​	mask：蒙版

```python 
from PIL import Image

a = Image.new('RGB', (300, 300), (255, 0, 0))  # 生成一张300*300的红色图片
b = Image.new('RGB', (200, 200), (0, 255, 0))  # 200*200的绿色图片
a.paste(b, (50, 50, 250, 250))  # 将b贴到a的坐标为（50，50）的位置
a.show()  # 显示a
```

