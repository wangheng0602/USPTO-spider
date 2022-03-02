from scrapy import cmdline

if __name__ == '__main__':
    cmd = 'scrapy crawl patentname'
    cmdline.execute(cmd.split())