# -*- coding: utf-8 -*-
import urllib
import scrapy
from simple_scrapy.items import SimpleScrapyItem

class DoubanBookSpiderSpider(scrapy.Spider):
    name = 'douban_book_spider'
    # 允许爬取的域名（如果遇到非该域名的url则爬取不到数据）
    allowed_domains = ['douban.com']
    # 起始爬取的url
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    # 爬取多页
    pageNum = 0  # 起始页码
    url = 'https://book.douban.com/tag/%s?start=%s&type=T'
    count = 0

    # 访问起始URL并获取结果后的回调函数，该函数的response参数就是向起始的url发送请求后，获取的响应对象.该函数返回值必须为可迭代对象或者NUll
    def parse(self, response):
        subject_lists = response.xpath('//*[@id="subject_list"]/ul')
        book_items=subject_lists.xpath('.//li[@class="subject-item"]')

        for book_item in book_items:
            self.count += 1
            book_info = book_item.xpath('.//div[@class="info"]')
            # 书名
            title = book_info.xpath('.//a[1]/@title').extract_first()
            book_detail_info = book_info.xpath('.//div[@class="pub"]/text()').extract_first().strip().split('/')

            # 作者/译者
            try:
                author_info = ''.join(book_detail_info[0:-3])
            except:
                author_info = '暂无'
            # 出版信息
            try:
                pub_info = ''.join(book_detail_info[-3:])
            except:
                pub_info = '暂无'
            # 评分
            try:
                rating = book_info.xpath('.//span[@class="rating_nums"]/text()').extract_first().strip()
            except:
                rating = '0.0'
            # 评价人数
            try:
                people_num = book_info.xpath('.//span[@class="pl"]/text()').extract_first().strip().strip('()人评价')
            except:
                people_num = '0'

            item = SimpleScrapyItem()
            item['sn_id'] = str(self.count)
            item['title'] = title
            item['author_info'] = author_info
            item['pub_info'] = pub_info
            item['rating'] = rating
            item['people_num'] = people_num

            yield item

        if self.pageNum <= 10:
            self.pageNum += 1
            next_url = format(self.url % (urllib.parse.quote('编程'), self.pageNum*20))

            # 递归爬取数据：callback参数的值为回调函数（将url请求后，得到的相应数据继续进行parse解析），递归调用parse函数
            yield scrapy.Request(url=next_url, callback=self.parse,dont_filter=False)

