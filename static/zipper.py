from zipfile import ZipFile
import os

def zipFiles(zipFolder = "VipulSnapper.zip", folder = "app"):

    with ZipFile(zipFolder,"w") as f:
        os.chdir(folder)
        for i in os.listdir():
            f.write(i)

if __name__ == "__main__":
    zipFiles()