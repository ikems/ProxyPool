"""
抓取到公用的代理后，需要对代理进行验证，然后再入库
"""

import datetime
import requests
import time
from multiprocessing.pool import ThreadPool
from save_to_db import SaveDB
from settings import target_website



def valid(proxy, method, url=target_website):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    proxies = {
        'http': 'http://' + proxy['proxyip'],
        'https': 'https://' + proxy['proxyip'],
    }
    try:
        start_time = time.time()
        #设置超时，如果超过10s也默认为访问失败
        resp = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
        #保留时间小数点后2位
        delay = round(time.time() - start_time, 2)
        #如果访问成功，则添加delay参数，如果不成功则设置为-1，表示无法访问
        if resp.status_code == 200:
            proxy['delay'] = delay
            # print(f'代理可用{proxy}')
            # 通过方法判断，抓取到的数据直接插入db，如果是检测ip值则是更新delay的值
            if method == 'spider':
                SaveDB().insert_proxy(proxy)
            elif method == 'check':
                SaveDB().update_proxy({'proxy': proxy['proxyip']}, {'delay': proxy['delay']})
        #检验时，返回其他类型，也删除该ip
        else:
            if method == 'check':
                SaveDB().delete_proxy({'proxyip': proxy['proxyip']})
            # print(f'代理不可用{proxy}')

    #对ip进行检验时，如果ip访问报错，
    except Exception:
        if method == 'check':
            SaveDB().delete_proxy({'proxyip': proxy['proxyip']})


def valid_many(proxy_list, method):
    pool = ThreadPool(10)
    # print(proxy_list)
    for proxy in proxy_list:
        pool.apply_async(valid, args=(proxy, method))
        # print(f'成功验证{proxy}可用性')
    #关闭线程池
    pool.close()
    #阻塞线程池，以免主线程退出
    pool.join()


def check_run():
    while True:
        m = SaveDB()
        count = m.get_count()
        if not count == 0:
            now = datetime.datetime.now()
            print(f'{now}开始验证数据库中代理ip：')
            proxies = m.get_proxy(count)
            valid_many(proxies, 'check')
        time.sleep(10*60)
