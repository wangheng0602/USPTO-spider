# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import os


class PatentPipeline(object):
    # 当需要把所有的专利文本保存到一个文件中时，可以使用被注释掉的方法
    '''
    def open_spider(self, spider):
        self.path = 'E:/火星无人机/专利/'+str(date2)
        self.f = open(self.path, 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.f.close()
    '''

    def open_spider(self, spider):
        self.date = datetime.datetime.today()
        date1 = self.date.__str__().replace(':', '.')
        # 创建存放专利的文件夹，以创建日期命名
        os.mkdir('E:/火星无人机/专利/' + date1)
        self.dir = 'E:/火星无人机/专利/' + str(date1)+'/'
        self.patentnum = open('E:/火星无人机/专利/'+str(date1)+'/patentnum.txt', 'w')

    def process_item(self, item, spider):

        # 将爬取的专利号保存到一个文本中
        self.patentnum.write(item['patentnum']+'\n')

        # 保存每个专利的具体信息
        self.path = self.dir + item['patentnum'] + '.txt'
        self.f = open(self.path, 'w', encoding='utf-8')
        self.f.write('patentnum' + ' ' + item['patentnum'] + '\n')
        self.f.write('title' + ' ' + item['title'] + '\n')
        self.f.write('category' + ' ' + item['category'] + '\n')
        self.f.write('abstract' + '\n' + item['abstract'] + '\n')
        content = ''
        for line in item['content']:
            content = content + line
        self.f.write('content' + '\n' + content+'\n'+'\n')
        self.f.close()
        return item

    def close_spider(self, spider):
        self.patentnum.close()
