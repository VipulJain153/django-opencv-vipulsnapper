from PIL import Image
import os

def readTransfromImages(imgPath = f"{os.path.abspath(os.path.dirname(__file__))}\\imgs", defaultFormat = "-1", newFormat = ".png") -> None:
    """
    This converts all the images ending with x format to y format
    """
    os.chdir(imgPath)
    for i in os.listdir():
        if i.endswith(defaultFormat) or defaultFormat == "-1":
            img = Image.open(i)
            name = os.path.splitext(i)[0]
            img.save(f'{name}{newFormat}')

if __name__ == "__main__":
    # print(os.path.realpath(__file__))
    # print(os.path.join(os.path.dirname(__file__), '..'))
    # print(os.path.abspath(os.path.dirname(__file__)))
    readTransfromImages()