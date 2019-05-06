import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

url = 'http://www.data5u.com/free/gngn/index.shtml'

headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'onnection': 'keep-alive',
            'Cookie': 'Hm_lvt_3406180e5d656c4789c6c08b08bf68c2=1556596607; UM_distinctid=16a6c6347b9299-015da963f0d915-366c7e04-13c680-16a6c6347bab4d; JSESSIONID=A4FC2E943DEAAD6D38CE87E556705E65; CNZZDATA1260383977=1630773375-1556595601-%7C1556644201; Hm_lpvt_3406180e5d656c4789c6c08b08bf68c2=1556648304',
            'Host': 'www.data5u.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }

resp = requests.get(url=url, headers=headers)
# options = webdriver.ChromeOptions()
# options.add_argument('User-Agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')

print(resp.text)