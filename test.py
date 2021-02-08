import requests

proxy = {'http': 'http://192.168.2.91:3080'}

se = requests.session()

ip = se.get('http://ifconfig.io', proxies=proxy).text

print(ip)
