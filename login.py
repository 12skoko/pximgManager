import requests
from bs4 import BeautifulSoup


se = requests.session()


def login(id, password):
    main_url= 'http://www.pixiv.net/'
    login_url = 'https://accounts.pixiv.net/login'
    # headers只要这两个就可以了,之前加了太多其他的反而爬不上
    headers = {
        'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3987.122 Safari/537.36'
    }
    pixiv_id = str(id)
    password = str(password)
    return_to = 'http://www.pixiv.net/'
    post_key = []
    post_key_html = se.get(login_url, headers=headers).text
    post_key_soup = BeautifulSoup(post_key_html, 'html.parser')
    post_key = post_key_soup.find('input')['value']
    # 上面是去捕获postkey
    datas = {
        'pixiv_id': pixiv_id,
        'password': password,
        'return_to': return_to,
        'post_key': post_key
    }
    data=bytes(urllib.parse.urlencode(datas),encoding="utf-8")
    L=se.post(login_url, data=data, headers=headers)
    response=se.get(main_url, headers=headers)
    # print("Login successfully!")


    # cookie_value = '1'
    # for key, value in L.cookies.values():
    #     cookie_value += key + '=' + value + ';'
    # headers['Cookie'] = cookie_value
    # print(cookie_value)
    cookie_value=''
    for key, value in response.cookies.items():
        cookie_value += key + '=' + value + ';'
    # headers['Cookie'] = cookie_value
    # print(cookie_value)


    cookies = response.cookies

    cookie = requests.utils.dict_from_cookiejar(cookies)
    print(cookie)

    cc = se.get('https://www.pixiv.net/ajax/user/41989573/profile/all?lang=zh', data=data, headers=headers,cookies=cookie).text
    print(cc)


ra=random.randint(0,1)
login('sakuraihatto@outlook.com', '1458987208')
login('Small_Week@outlook.com', '1458987208')
