import os


def readname():
    filePath = r'F:\pixiv\[bookmark] Public'
    name = os.listdir(filePath)
    return name


if __name__ == "__main__":
    listName = []
    name = readname()
    print(name)
    for i in name:
        print(i)