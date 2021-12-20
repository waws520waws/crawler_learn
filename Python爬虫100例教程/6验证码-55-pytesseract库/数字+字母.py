import pytesseract
from PIL import Image


def main():
    image = Image.open("1.png")

    text = pytesseract.image_to_string(image, lang="chi_sim")
    print(text)


if __name__ == '__main__':
    main()
