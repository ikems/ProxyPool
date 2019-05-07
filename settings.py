"""
定义爬取不同网站的规则，以及所需的参数
"""

config_lists = [
    {
    'name': '快代理',
    'urls': [f'https://www.kuaidaili.com/free/inha/{i}/' for i in range(1,10)],
    'type': 'xpath',
    'pattern': '//tbody/tr',
    'target': {'ip': 'td[1]', 'port': 'td[2]'},
    'delay': 1.5,
    'download_type': 'normal'
    },

    {
    'urls': [f'http://www.66ip.cn/{k}.html' for k in range(1, 6)],
    'type': 'xpath',
    'pattern': '//*[@id="main"]//tbody/tr',
    'target': {'ip': './td[1]', 'port': './td[2]'},
    'download_type': 'selenium',
    'delay': 1.5,
    },

    {
    'urls': [f'https://www.xicidaili.com/nn/{j}' for j in range(1, 6)],
    'type': 'xpath',
    'pattern': '//table/tr',
    'target': {'ip': 'td[2]', 'port': 'td[3]'},
    'download_type': 'normal',
    },

    {
    'urls': ['http://www.data5u.com/free/gngn/index.shtml'],
    'type': 'xpath',
    'pattern': '//ul[@class="l2"]',
    'target': {'ip': './span[1]/li', 'port': './span[2]/li'},
    'download_type': 'selenium',
    'delay': 1.5,
    }

]

#所需要爬取的目标网站，即使用代理对其访问进行验证
target_website = 'https://www.baidu.com'