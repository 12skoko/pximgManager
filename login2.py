import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import http.cookiejar
import requests


def login(id, password):
    main_url = 'http://www.pixiv.net/'
    login_url = 'https://accounts.pixiv.net/login'
    # headers只要这两个就可以了,之前加了太多其他的反而爬不上
    head = {
        'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3987.122 Safari/537.36'
    }
    pixiv_id = str(id)
    password = str(password)
    return_to = 'http://www.pixiv.net/'
    post_key = []
    request = urllib.request.Request(login_url, headers=head)
    response = urllib.request.urlopen(request)
    post_key_html = response.read().decode("utf-8")
    post_key_soup = BeautifulSoup(post_key_html, 'html.parser')
    post_key = post_key_soup.find('input')['value']
    # 上面是去捕获postkey
    # print(post_key)
    datas = {
        'pixiv_id': pixiv_id,
        'password': password,
        'return_to': return_to,
        'post_key': post_key
    }
    data=bytes(urllib.parse.urlencode(datas),encoding="utf-8")
    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.LWPCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(login_url, headers=head)
    try:
        response = opener.open(request, data=data)
    except urllib.error.URLError as e:
        print(e.reason)

    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    for item in cookie:
        print('Name = ' + item.name)
        print('Value = ' + item.value)
    # cookie['PHPSESSID']='62707046_96gao5aUhg1mh2B9KCbmeqR4mO2BgGQR'
    datas2={
        'pixiv_id': pixiv_id,
        'password': password,
        'return_to': return_to,
        'post_key': post_key,
        'cookies':cookie
    }
    datas=bytes(urllib.parse.urlencode(datas2),encoding="utf-8")

    se = requests.session()
    cc = se.get('https://www.pixiv.net/ajax/user/41989573/profile/all?lang=zh', data=datas, headers=head,cookies=cookie).text
    print(cc)
    # request=urllib.request.Request('https://www.pixiv.net/ajax/user/41989573/profile/all?lang=zh',headers=head,data=datas)
    # json=urllib.request.urlopen(request)
    #
    # print(json)
    # cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
    # request = urllib.request.Request(login_url, data=data, headers=head)
    # response = urllib.request.urlopen(request)
    #
    #
    # handler = urllib.request.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    # opener = urllib.request.build_opener(handler)  # 通过handler来构建opener
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)

#     cookie = http.cookiejar.CookieJar()
#     # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
#     handler = urllib.request.HTTPCookieProcessor(cookie)
#     # 通过handler来构建opener
#     opener = urllib.request.build_opener(handler)
#     # 此处的open方法同urllib2的urlopen方法，也可以传入request
#     request = urllib.request.Request(login_url, data=datas, headers=head)
#
#     response = opener.open(request)
#
#     cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
#     for item in cookie:
#         print('Name = ' + item.name)
#         print('Value = ' + item.value)
#
login('sakuraihatto@outlook.com','1458987208')
