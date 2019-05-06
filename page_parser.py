"""
根据指定的爬取规则获取相应页面的
"""

from lxml import etree
import traceback
import re


class PageParser(object):
    #定义好解析的方法和路径后，可以对页面采用通用的解析模式
    #不同类型的解析函数之间互不干扰，设置为静态方法，无需实例化即可调用
    @staticmethod
    def xpath_parse(resp, parse_rule):
        try:
            page = etree.HTML(resp)
            proxies = page.xpath(parse_rule['pattern'])
            # print(parse_rule['pattern'])
            proxy_list = []
            for i in proxies[1:]:
                ip = i.xpath(parse_rule['target']['ip'])[0].text
                # print(ip)
                port = i.xpath(parse_rule['target']['port'])[0].text
                # print(port)
                proxy = {'proxyip': ip + ':' + port}
                proxy_list.append(proxy)
            return proxy_list
        except Exception:
            traceback.print_exc()

    @staticmethod
    def re_parser(resp, parse_rule):
        try:
            proxies = re.findall(parse_rule['pattern'], resp, re.S)
            proxy_list = []
            for i in proxies[1:]:
                ip = re.findall(parse_rule['target']['ip'], i, re.S)[0]
                port = re.findall(parse_rule['target']['port'], i, re.S)[0]
                #以字典的形式传输，为了在数据库存储中为ip设置更多的属性，如延迟时间，代理自身的分数等等
                proxy = {'proxyip': ip + ':' + port}
                proxy_list.append(proxy)
            return proxy_list
        except Exception:
            traceback.print_exc()

    # 通过判断网页解析的方式选择对应的解析方法
    def parse(self, resp, parse_rule):
        if parse_rule['type'] == 'xpath':
            return self.xpath_parse(resp, parse_rule)
        elif parse_rule['type'] == 're':
            return self.re_parser(resp, parse_rule)