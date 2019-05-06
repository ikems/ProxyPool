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
    'delay': 1.5
    },

    # {
    # 'urls': [f'http://www.66ip.cn/{i}.html' for i in range(1, 6)],
    # 'type': 'xpath',
    # 'pattern': '//div[@id="main"]//table/tr',
    # 'target': {'ip': 'td[1]', 'port': 'td[2]'},
    # },

    {
    'urls': [f'https://www.xicidaili.com/nn/{j}' for j in range(1, 6)],
    'type': 'xpath',
    'pattern': '//table/tr',
    'target': {'ip': 'td[2]', 'port': 'td[3]'},
    },

    # {
    # 'urls': ['http://www.data5u.com/free/gngn/index.shtml'],
    # 'type': 'xpath',
    # 'pattern': '//li[@style="text-align:center;"]/ul',
    # 'target': {'ip': 'span[1]', 'port': 'span[2]'},
    # },


]