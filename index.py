import requests
from pixivpy3 import *
import re
from bs4 import BeautifulSoup
import os
import sqlite3
import time


def readname():
    filePath = r'F:\pixiv\[bookmark] Public'
    name = os.listdir(filePath)
    return name


def readnumlist():
    list = readname()
    list = str(list)
    re_num = re.compile('\((\w*)\).*?[.jpg|.png]')
    list_num = re.findall(re_num, list)
    return list_num


def get_illust_data(id):
    se = requests.session()
    head = {
        'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3987.122 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    url = 'https://www.pixiv.net/artworks/' + str(id)
    html = se.get(url, headers=head).text
    html_temp = BeautifulSoup(html, 'html.parser')
    content = html_temp.select('meta[id="meta-preload-data"]')
    content = str(content)
    illust_data = []
    re_1 = re.compile(',"id":"(.*?)","title":"(.*?)","description":"(.*?)","illustType":\w*,"createDate":"(.*?)","uploadDate":"')
    re_2 = re.compile('"storableTags":\[.*?\],"userId":"(.*?)","userName":"(.*?)","userAccount":".*?","userIllusts":')
    re_3 = re.compile('"likeData":.*?,"width":(.*?),"height":(.*?),"pageCount":(.*?),"bookmarkCount":(.*?),"likeCount":(.*?),"commentCount":(.*?),"responseCount":.*?,"viewCount":(.*?),')
    try:
        part1 = re.search(re_1, content)
        part2 = re.search(re_2, content)
        part3 = re.search(re_3, content)
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

        # for i in range(0,13):
        # print(illust_data[i])
        return illust_data
    except:
        illust_data.append(0)
        return illust_data


def sqlstring(illust_data):
    string = "insert into bookmark(id,pageCount,name,author_id,auther_name,width,height,bookmarkCount,likeCount,commentCount,viewCount,createtime,descriotion)"
    string += "values("
    for i in range(0, 12):
        if i == 2 or i == 4 or i == 11:
            string += "'"
            string += str(illust_data[i]) + "',"
        else:
            string += str(illust_data[i]) + ","
    string += "'" + str(illust_data[12]) + "');"
    return string


conn = sqlite3.connect("pixiv.db")
list_num = readnumlist()
num = len(list_num)
# try:
for i in range(0, num):
    print(str(i + 1) + '/' + str(num))
    print(list_num[i])
    if i == 0 or list_num[i] != list_num[i - 1]:
        illust_data = get_illust_data(list_num[i])
        if illust_data[0]==0:
            print('pass')
            continue
        sqlstringexecute = sqlstring(illust_data)
        conn.execute(sqlstringexecute)
        time.sleep(0.1)
    else:
        pass
    if i%100==0:
        conn.commit()

# except:
#      print('error')
#      print(sqlstring)

# for i in range(0, num):
#     print(list_num[i])
# illust_data=get_illust_data(78654343)
# sqlstring=sqlstring(illust_data)
# print(sqlstring)
# conn.execute(sqlstring)

conn.commit()
conn.close()
