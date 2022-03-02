import os
import shutil



patent_path = 'E:/火星无人机/专利/DOWNLOAD/16-20patent/'
vec_path = 'E:/火星无人机/专利/DOWNLOAD/vector/'
untreated_path = 'E:/火星无人机/专利/DOWNLOAD/untreated/'
patentlist = []
patentvec = []
for _, _, name in os.walk(patent_path):
    for f in name:
        patentlist.append(f)

for _, _, vec in os.walk(vec_path):
    for f in vec:
        patentvec.append(f)

i = 0
for a in patentvec:
    patentlist.remove(a)
    i = i + 1
    print('\r', '进度：{:.6f}'.format(i / len(patentvec)), end='', flush=True)
print('\n')

b = 0
for patent in patentlist:
    b = b + 1
    source = patent_path + patent
    target = untreated_path + patent
    shutil.copyfile(source, target)
print(b)


'''
def spilt_doc(patentlist, path):
    for patent in patentlist:
        source = patent_path + patent
        target = path + patent
        shutil.copyfile(source, target)


patent_path = 'E:/火星无人机/专利/DOWNLOAD/untreated/'
untreated_path = 'E:/火星无人机/专利/DOWNLOAD/untreated'
patentlist = []
for _, _, name in os.walk(patent_path):
    for f in name:
        patentlist.append(f)
print(len(patentlist))

for c in range(5):
    print('开始复制到第'+str(c)+'个文件夹')
    if c == 4:
        m = c * 200000
        patent = patentlist[m:]
        path = untreated_path + str(c) + '/'
        spilt_doc(patent, path)
    else:
        m = c*200000
        n = (c+1)*200000
        patent = patentlist[m: n]
        path = untreated_path + str(c) + '/'
        spilt_doc(patent, path)
'''