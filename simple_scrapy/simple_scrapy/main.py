from scrapy import cmdline

# 输出未过滤的页面信息
cmdline.execute('scrapy crawl douban_book_spider'.split())