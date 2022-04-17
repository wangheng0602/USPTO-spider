# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
import pymysql
from config import config


class UsptoSpiderPipeline:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",password="wh1046106652",database="uspto")
        keyword = config['keyword']
        date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
        self.table_name = keyword + date
        self.cursor = self.db.cursor()

    def open_spider(self, spider):
        # 创建表
        self.cursor.execute("drop table if exists " + self.table_name)
        sql = "create table " + self.table_name + \
            " (patentnum varchar(20) primary key, title varchar(1000), category varchar(1000), \
            abstract text, content mediumtext)"

        print('创建sql表: ----', sql)
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        # 插入数据
        if (item['patentnum'] is None) or (item['title'] is None) or (item['category'] is None)\
                    or (item['abstract'] is None) or (item['content'] is None):
            print('-------------数据为空----------')
        else:
            data = (item['patentnum'], item['title'], item['category'], item['abstract'], str(item['content']))
            sql = "insert into " + self.table_name + " values(%s, %s, %s, %s, %s)"
            print('插入数据', sql)
            self.cursor.execute(sql, data)
            self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()