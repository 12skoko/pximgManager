import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import html
from lxml.html import fromstring
import cssselect
from lxml.html import etree
import random


se = requests.session()


def parse_form(html):
    tree=fromstring(html)
    data={}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')]=e.get('value')
    return data


def login(id, password):
    main_url= 'http://www.pixiv.net/'
    login_url = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page'
    # headers只要这两个就可以了,之前加了太多其他的反而爬不上
    headers = {
        'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3987.122 Safari/537.36'
    }
    html=se.get(login_url,headers=headers)
    data=parse_form(html.content)
    data['pixiv_id']=id
    data['password']=password
    response=se.post(login_url,data=data,headers=headers)
    print(response.cookies.keys())
    print(response.cookies.values())
    sec_response=se.get(main_url,data=data,headers=headers,cookies=response.cookies)
    print(sec_response.cookies.keys())
    print(sec_response.cookies.values())
    json=se.get('https://www.pixiv.net/ajax/user/41989573/profile/all?lang=zh', data=data, headers=headers,cookies=sec_response.cookies).text
    print(json)



ra=random.randint(0,2)
if ra == 1:
    print(1)
    login('sakuraihatto@outlook.com', '1458987208')
else :
    if ra == 2:
        print(2)
        login('Small_Week@outlook.com', '1458987208')
    else:
        print(0)
        login('12skoko1458987208@gmail.com', '1458987208')