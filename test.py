import requests
from bs4 import BeautifulSoup
import re


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
    # print(content)

    re_tag = re.compile('\{\"tag\":\"([^\"]*?)\",\"locked\":(true|false),\"deletable\":(true|false)(,\"userId\":\"\d*?\")?(,\"translation\":{\"[^\"]*?\":\"(.*?)\"\})?')
    tags_temp = re.findall(re_tag, content)
    tags=''
    for i in tags_temp:
        tags+=i[0]
        print(i[0],end='')
        if i[5]!='':
            print('('+i[5]+')')
            tags+='('+i[5]+')'
        tags+=','
    tags.strip(',')
    print(tags)



get_illust_data(84689812)


# \{\"tag\":\"([^\"]*?)\",\"locked\":(true|false),\"deletable\":(true|false(,\"userId\":\"\d*?\")?),(\"translation\":{\".*?\":\"(.*?)\"\})
# \{\"tag\":\"([^\"]*?)\",\"locked\":(true|false),\"deletable\":(true|false,\"userId\":\"\d*?\")}

# \{\"tag\":\"([^\"]*?)\",\"locked\":(true|false),\"deletable\":(true|false)(,\"userId\":\"\d*?\")?(,\"translation\":{\"[^\"]*?\":\"(.*?)\"\})?