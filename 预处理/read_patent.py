import pandas as pd


path = 'E:/火星无人机/专利/DOWNLOAD/16-20patent/'
test = pd.read_table("E:/火星无人机/专利/download/brf_sum_text_2020.tsv", low_memory=False)
patentnum = test['patent_id']
text = test['text']
l = len(patentnum)
print(l)
m = 0
for i in range(len(patentnum)):
    m = m + 1
    print('\r', '进度：{:.5f}'.format(i / l), end='', flush=True)  # 用于进度展示
    f = open(path+str(patentnum[i])+'.txt', 'w', encoding='utf-8')
    f.write(text[i])
    f.close()


