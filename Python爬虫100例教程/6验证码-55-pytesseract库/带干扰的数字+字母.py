import pytesseract
from PIL import Image


def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def main():
    image = Image.open("2.png")

    image = image.convert('L')

    binaryImage = image.point(initTable(), '1')
    binaryImage.save('3.png')
    # binaryImage.show()

    # 这里为识别出来（因为是带干扰的图片）
    text = pytesseract.image_to_string(binaryImage, lang="chi_sim")
    print(text)


if __name__ == '__main__':
    main()
