import re
import requests
import datetime
import os
import requests
import random


url = 'http://icanhazip.com/'
proxy = 'http://34.203.248.159:80'
res = requests.get(url, proxies={"http": proxy}).text.replace('\n', '')
print(res)
print(type(res))
ip = proxy.split(':')[1].replace(r'//', '')
print(ip)
print(type(ip))
if (res == ip):
    print("代理IP:'" + res + "'有效！")

'''
headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'
        }
url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
res = requests.get(url, headers=headers).text
print(res)
'''