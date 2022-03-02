import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from patent.items import PatentItem

class PatentnameSpider(CrawlSpider):
    name = 'patentname'
    allowed_domains = ['patft.uspto.gov']
    # 起始url对于不同的关键词不同
    start_urls = ['https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1\
                &u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=UAV&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT']

    rules = (
        # 处理每一个专利具体内容的链接
        Rule(LinkExtractor(allow='/netacgi/.*s1=.*[^Page=Next]&OS=.*&RS=.*'), callback='parse_item', follow=True),
        # 处理下一页的链接
        Rule(LinkExtractor(allow='/netacgi/.*s1=.*[Page=Next]&OS=.*&RS=.*'), callback='parse_page', follow=True)
    )

    def parse_item(self, response):
        # print(response.meta['proxy'])
        item = PatentItem()
        item['patentnum'] = response.xpath("//body/table/tr[1]/td[2]/b[1]//text()").get()
        item['title'] = response.xpath("//body/font[1]//text()").get()
        item['category'] = response.xpath("//b[contains(text(),'Current International Class:')]\
                                            /parent::*/following-sibling::*//text()").get()
        item['abstract'] = response.xpath("//body//p[1]//text()").get()
        # 有些论文详情页没有coma标签，因此替换为下一种定位方式
        # item['content'] = response.xpath("//html//body//coma//text()").getall()
        item['content'] = response.xpath("//center[contains(.//text(), 'Description')]/following::text()").getall()
        return item

    def parse_page(self, response):
        pass
