# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PatentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    patentnum = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    abstract = scrapy.Field()
    content = scrapy.Field()
