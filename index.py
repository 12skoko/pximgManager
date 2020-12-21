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
    illust_data=[]
    re_1=re.compile(',"id":"(.*?)","title":"(.*?)","description":"(.*?)","illustType":0,"createDate":"(.*?)","uploadDate":"')
    part1=re.search(re_1,content)
    re_2=re.compile('"storableTags":\[.*?\],"userId":"(.*?)","userName":"(.*?)","userAccount":".*?","userIllusts":')
    part2=re.search(re_2,content)
    re_3=re.compile('"likeData":.*?,"width":(.*?),"height":(.*?),"pageCount":(.*?),"bookmarkCount":(.*?),"likeCount":(.*?),"commentCount":(.*?),"responseCount":.*?,"viewCount":(.*?),')
    part3=re.search(re_3,content)
    illust_data.append(part1[1])
    illust_data.append(part3[3])
    illust_data.append(part1[2])
    illust_data.append(part2[1])
    illust_data.append(part2[2])
    illust_data.append(part3[1])
    illust_data.append(part3[2])
    illust_data.append(part3[4])
    illust_data.append(part3[5])
    illust_data.append(part3[6])
    illust_data.append(part3[7])
    illust_data.append(part1[4])
    illust_data.append(part1[3])
    for i in range(0,13):
        print(illust_data[i])
    return illust_data



list=readname()
list=str(list)
re_num=re.compile('\((\w*)\)')
list_num=re.search(re_num,list)
try:
    for i in range(1,1000):
        print(list_num[i])
except:
    print('end')
# for i in list:
    # print(i)



# conn=sqlite3.connect('pixiv.db')
# c=conn.cursor()
#
#
# c=conn.close()
