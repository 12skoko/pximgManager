import requests
from pixivpy3 import *
import os
import sqlite3


def readname():
    filePath = r'F:\pixiv\[bookmark] Public'
    name = os.listdir(filePath)
    return name

conn=sqlite3.connect('pixiv.db')
c=conn.cursor()

