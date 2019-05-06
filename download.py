"""
下载相应代理网站的网页，返回内容
"""

import requests
import chardet
import traceback
import time


class Downloader(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }


    def page_download(self, url, conf):
        # print(f'正在下载:{conf['name']}网站')
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
            # print(f'下载{conf['name']}出错')
            traceback.print_exc()



