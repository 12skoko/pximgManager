import re
import requests
from bs4 import BeautifulSoup

se = requests.session()
def get_member_illust(id):
    member_illust_url='https://www.pixiv.net/ajax/user/'+str(id)+'/profile/all'
    headers = {
        'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    member_illust=se.get(member_illust_url, headers=headers).text
    print(member_illust)


