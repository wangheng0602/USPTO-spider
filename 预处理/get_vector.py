import requests
import os
import re
import time

'''
params = {'clientId': '1399692722679345152', 'secretKey': '3e7a9c691b83674c96bfc45851493bc7'}
url = 'https://wudaoai.cn/model-api/api/v2/auth'
res = requests.post(url=url, params=params, headers={'AccessToken': '3e7a9c691b83674c96bfc45851493bc7'})
print(res.text)
'''

patent_path = 'E:/火星无人机/专利/DOWNLOAD/untreated/'
vec_path = 'E:/火星无人机/专利/DOWNLOAD/vector/'
patentlist = []
url = 'http://120.92.50.21:6175/text_query'
# 获取路径文件夹下专利名称，存入列表
for _, _, name in os.walk(patent_path):
    for f in name:
        patentlist.append(f)


def get_vector():
    # 判断那些专利已经被表示为向量
    patentvec = []
    for _, _, name2 in os.walk(vec_path):
        for v in name2:
            patentvec.append(v)
    print(len(patentvec))
    i = 0
    for patent in patentlist:
        i = i + 1
        if patent in patentvec:
            pass
        else:
            content = ''
            f = open(patent_path+patent, 'r', encoding='utf-8')
            for line in f:
                content = content+line
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            res = s.get(url=url, params={'text': content}, timeout=4)
            vector = re.compile(r'(?<="embedding":).+(?=})')
            vec = vector.findall(res.text)
            fvec = open(vec_path+patent, 'w', encoding='utf-8')
            fvec.write(vec[0])
            fvec.close()
        print('\r', '进度：{:.6f}'.format(i / len(patentlist)), end='', flush=True)  # 用于进度展示


if __name__ == '__main__':
    for _ in range(10000):
        if len(os.listdir(vec_path)) < 1560000:
            print('还未完全转换')
            # get_vector()

            try:
                print('开始转换')
                get_vector()
            except:
                time.sleep(60)
                print('\n'+'Error')
                continue
        else:
            break


