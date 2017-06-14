# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class download_spider(CrawlSpider):
    data = dict()
    name = 'wiki'
    allowed_domains = ['simple.wikipedia.org']
    start_urls = [
        "http://simple.wikipedia.org/wiki/",
    ]
    rules = (
        Rule(LinkExtractor(allow=('/wiki/'), deny=('/wiki/Special:',
                                                    '/wiki/User:',
                                                    '/wiki/Wikipedia:',
                                                    '/wiki/WP:',
                                                    '/wiki/WT:',
                                                    '/wiki/Project:',
                                                    '/wiki/File:',
                                                    '/wiki/MediaWiki:',
                                                    '/wiki/Template:',
                                                    '/wiki/Help:',
                                                    '/wiki/Portal:',
                                                    '/wiki/Book:',
                                                    '/wiki/Draft:',
                                                    '/wiki/Education Program:',
                                                    '/wiki/TimedText:',
                                                    '/wiki/Module:',
                                                    '/wiki/Topic:',
                                                    '/wiki/Gadget:',
                                                    '/wiki/Gadget definition:',
                                                    '/wiki/Image:',
                                                    '/wiki/Talk:',
                                                    '/wiki/Wikipedia talk:',
                                                    '/wiki/User_talk:',
                                                    '/wiki/Wikipedia_talk:',
                                                    '/wiki/Category_talk:',
                                                    '/wiki/Template_talk:',
                                                    )), callback='parse_start_url', follow=True),
    )
    fname = 0

    def parse_start_url(self, response):
        self.fname += 1
        fname = r'C:\Users\marte_000\Desktop\ucheba\8_semestr\inf_poisk\hw1\inf_poisk\files2\%s.html' % self.fname
        self.data[self.fname] = response.url

        with open(fname, 'w') as f:
            f.write('%s\n' % response.body)

    def __init__(self, *a, **kw):
        super(download_spider, self).__init__(*a, **kw)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        result_id = []
        for key in self.data.keys():
            result_id.append(str(key) + '.html' + '\t' + str(self.data[key]))
        with open('urls.txt', 'w') as f:
            f.write('\n'.join(result_id))