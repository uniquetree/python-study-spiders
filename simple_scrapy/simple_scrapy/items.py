# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SimpleScrapyItem(scrapy.Item):
    sn_id = scrapy.Field()
    title = scrapy.Field()
    author_info = scrapy.Field()
    pub_info = scrapy.Field()
    rating = scrapy.Field()
    people_num = scrapy.Field()

