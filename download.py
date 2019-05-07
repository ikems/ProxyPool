"""
下载相应代理网站的网页，返回内容
"""

import requests
import chardet
import traceback
import time
from selenium import webdriver
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Downloader(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.wait = WebDriverWait(self.browser, 10)


    def page_download(self, url, conf):
        print(f'正在下载:{url}网站')
        try:
            resp = requests.get(url=url, headers=self.headers)
            # 猜测返回页面的编码格式，概率，以及所使用的语言
            # chardet方法用于获取页面的编码方式
            resp.encoding = chardet.detect(resp.content).get('encoding')

            if conf.get('delay'):
                time.sleep(conf.get('delay'))

            if resp.status_code == 200:
                return resp.text
            else:
                raise ConnectionError


        except Exception:
            print(f'下载{url}出错')
            traceback.print_exc()


    def sele_download(self, url, conf):
        print(f'正在下载:{url}网站')
        self.browser.get(url=url)

        if conf.get('delay'):
            time.sleep(conf.get('delay'))

        html = self.browser.page_source

        if html:
            return html
        else:
            self.sele_download(url=url)
        self.browser.close()

    # 通过判断网页下载的方式选择对应的下载方法
    def download(self, url, conf):
        if conf['download_type'] == 'normal':
            return self.page_download(url=url, conf=conf)
        elif conf['download_type'] == 'selenium':
            return self.sele_download(url=url, conf=conf)








