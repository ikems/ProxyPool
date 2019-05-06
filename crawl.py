"""
运行爬虫
"""


import datetime
import time

from settings import config_lists
from download import Downloader
from page_parser import PageParser
from validate import valid, valid_many


def crawl_run():
    while True:
        now = datetime.datetime.now()
        print(f'{now}开始抓取代理ip：')
        c = Crawler()
        c.crawl()
        time.sleep(30*60)


class Crawler(object):
    def crawl(self):
        for conf in config_lists:
            for url in conf['urls']:
                resp = Downloader().page_download(url, conf)
                if resp:
                   proxy_list = PageParser().parse(resp, conf)
                   # print(proxy_list)
                   print('正在验证代理可以用性')
                   valid_many(proxy_list, 'spider')


