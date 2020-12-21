import requests
from pixivpy3 import *
import re
from bs4 import BeautifulSoup
import os
import sqlite3


def readname():
    filePath = r'F:\pixiv\[bookmark] Public'
    name = os.listdir(filePath)
    return name


def get_illust_data(id):
    se=requests.session()
    head={
        'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3987.122 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    url='https://www.pixiv.net/artworks/'+str(id)
    html = se.get(url, headers=head).text
    html_temp = BeautifulSoup(html, 'html.parser')
    content = html_temp.select('meta[id="meta-preload-data"]')
    content=str(content)
    re_id=re.compile(',"illust":\{"(\w*?)":\{"illustId":"')
    id=re.search(re_id,content)
    illust_data=[]
    illust_data[0]=id[1]
    print(id[1])

    # print(html)



get_illust_data(70441587)



# conn=sqlite3.connect('pixiv.db')
# c=conn.cursor()
#
#
# c=conn.close()
