import re
import requests
import os
import shutil
'''
url = 'https://wudaoai.cn/model-api/api/v1/auth'
params = {'clientId': '1399692722679345152', 'secretKey': '3e7a9c691b83674c96bfc45851493bc7'}
s = requests.session()
s.keep_alive = False  # 关闭多余连接
res = s.post(url=url, params=params, timeout=4)
print(res.text)
'''

for c in range(5):
     m = c * 200000
     print(m)
     print(type(m))