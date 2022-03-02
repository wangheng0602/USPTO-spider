"""用于将爬取到的原始文件按照项目分别进行保存"""
import os
import re


raw_path = 'E:/火星无人机/专利/2021-05-21 20.34.55.184837/'
item_path = 'E:/火星无人机/专利/'
patentlist = []

# 获取路径文件夹下专利名称，存入列表
for _, _, name in os.walk(raw_path):
    for f in name:
        patentlist.append(f)


# 读取第i个专利文本的内容
def read_patent(i):
    text = ''
    patent = open(raw_path + patentlist[i], 'r', encoding='utf-8')
    for line in patent:
        text = text + line.replace('\n', '')
    patent.close()
    return text


# 根据输入的item对文件进行保存
def save_item(item, i, text):
    if not os.path.isdir(item_path + item):
        os.mkdir(item_path + item)
    # 判断正则表达式匹配出来的文本是否正确
    if item == 'category':
        if len(text[0]) > 1000:  # category长度异常的阈值
            print('请检查 '+patentlist[i]+' 的 '+item)
    if item == 'title':
        if len(text[0]) > 200:  # title长度异常的阈值
            print('请检查 '+patentlist[i]+' 的 '+item)
    if item == 'abstract':
        if len(text[0]) > 2000:  # abstract长度异常的阈值
            print('请检查 '+patentlist[i]+' 的 '+item)
    # 保存文本
    f = open(item_path + item + '/' + patentlist[i], 'w')
    f.write(text[0])
    f.close()


def get_item(item, patentlist):
    all_text = ''
    for i in range(len(patentlist)):
        all_text = all_text+read_patent(i)
    if item == 'patentnum':
        f = open(item_path + item + '.txt', 'w')
        num = re.compile(r'(?<=patentnum )\d+,\d+,\d+')
        patentnum = num.findall(all_text)
        for i in range(len(patentnum)):
            f.write(patentnum[i]+'\n')
        f.close()
    else:
        for i in range(len(patentlist)):
            text = read_patent(i)
            if item == 'category':
                exp = re.compile('(?<=category ).+?(?=abstract)')
                category = exp.findall(text)
                save_item(item=item, i=i, text=category)
            if item == 'title':
                exp = re.compile('(?<=title ).+?(?=category)')
                title = exp.findall(text)
                save_item(item=item, i=i, text=title)
            if item == 'abstract':
                exp = re.compile('(?<=abstract ).+?(?=content)')
                abstract = exp.findall(text)
                save_item(item=item, i=i, text=abstract)
            if item == 'content':
                exp = re.compile(r'(?<=content ).+?(?=\* \* \* \* \* )')
                content = exp.findall(text)
                save_item(item=item, i=i, text=content)


if __name__ == '__main__':
    get_item('category', patentlist)
    get_item('title', patentlist)
    get_item('abstract', patentlist)
    get_item('content', patentlist)
