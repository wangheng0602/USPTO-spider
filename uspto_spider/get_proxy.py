import requests
import re
import random


class GetProxy(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 \
            (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'
        }
        self.url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
        self.proxy = 'http://183.88.226.50:8080'

    # 从网页获取原始代理列表，存入proxylist中
    def get_proxy(self):
        ip = re.compile(r'(?<=export_address": \[")\d+\.\d+\.\d+\.\d+')
        prot = re.compile(r'(?<=port": )\d+')
        httptype = re.compile(r'(?<=type": ")\w+')
        res = requests.get(self.url, headers=self.headers, proxies={"http": self.proxy, "https": self.proxy}).text
        # print(res)
        proxylist = []
        for line in res.split('\n'):
            address = str(ip.findall(line)).replace('[', '').replace(']', '').replace("'", '')
            prot1 = str(prot.findall(line)).replace('[', '').replace(']', '').replace("'", '')
            http = str(httptype.findall(line))
            if address:
                if http == "['https']":
                    proxy = 'https://' + address + ':' + prot1
                else:
                    proxy = 'http://' + address + ':' + prot1
                proxylist.append(proxy)
        print('已获取到原始代理'+'数量为：'+str(len(proxylist)))
        f = open('./proxy_list.txt', 'w')
        for line in proxylist:
            f.write(line+'\n')
        f.close()

    # 对获取的代理列表进行筛选，返回有效代理
    def fliter_proxy(self):
        proxylist = []
        f = open('./proxy_list.txt', 'r')
        for line in f:
            proxylist.append(line)
        f.close()
        a = 0
        b = 0
        f = open('./proxy_list.txt', 'w')
        for num in range(len(proxylist)):
        # for num in range(100):
            proxy = proxylist[num].replace('\n', '')
            try:
                # print('原始ip:' + proxy)
                res = requests.get(url="https://patft.uspto.gov/", timeout=4, headers=self.headers,
                                   proxies={"http": proxy, "https": proxy})
                # proxyip = res.text.replace('\n', '')
                # print('验证网页返回的ip：'+proxyip)
                if res.status_code == 200:
                    print('该代理：'+proxy+'有效!正在存入文件...')
                    a = a+1
                # ip = proxy.split(':')[1].replace(r'//', '')
                # if (proxyip == ip):
                    f.write(proxy+'\n')
            except:
                b = b+1
                print('该代理：'+proxy+'无效!')
        f.close()
        print('有效代理个数：'+str(a))
        print('无效代理个数：' + str(b))

    # 验证某个代理是否有效
    def check_proxy(self, proxy):
        try:
            res = requests.get(url="https://patft.uspto.gov/",
                               timeout=4, headers=self.headers, proxies={"http": proxy, "https": proxy})
            if res.status_code == 200:
                print('该ip：'+proxy+' 有效！')
        except:
            print('该ip：'+proxy+' 无效')


if __name__ == '__main__':
    i = GetProxy()
    # i.get_proxy()
    # for _ in range(4):
    #     i.fliter_proxy()


    proxylist = open('./proxy_list.txt', 'r')
    usefullproxy = []
    for line in proxylist:
        usefullproxy.append(line.replace('\n', ''))
    print(usefullproxy)
    print(len(usefullproxy))
    for proxy in usefullproxy:
        i.check_proxy(proxy)


