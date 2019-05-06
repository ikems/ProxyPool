import pymongo
from pymongo.errors import DuplicateKeyError


class SaveDB(object):
    def __init__(self):
        #生成mongodb对象，链接数据库
        self.client = pymongo.MongoClient()
        #指定数据库
        self.db = self.client['proxypool']
        #指定集合
        self.proxies = self.db['proxies']
        # 为ip去重,设置主键
        self.proxies.create_index('proxyip', unique=True)

    #插入数据
    def insert_proxy(self, proxy):
        try:
            self.proxies.insert_one(proxy)
            print(f'插入成功：{proxy}')
        except DuplicateKeyError:
            pass


    def delete_proxy(self, conditions):
        self.proxies.remove(conditions)
        print(f'删除成功：{conditions}')


    def update_proxy(self, conditions, value):
        self.proxies.update(conditions, {"$set": value})
        print(f'更新{conditions}的数据为{value}')


    # 从数据库中查找出指定数量的ip
    def get_proxy(self, count):
        count = int(count)
        #每次查找时，以delay做升序排列，时间越小，排名越靠前
        #此sort不是python自带的方法，是mongodb中对course对象的方法
        #{'_id':0}查找时，不返回id
        items = self.proxies.find({},{'_id':0},limit=count).sort(
            'delay', pymongo.ASCENDING
        )
        # print(items)
        items = [{'proxyip': i['proxyip']} for i in items]
        # print(items)
        return items


    #添加一个获取数据库中现有ip数量的方法
    #conditions为以后的扩展条件
    def get_count(self, conditions=None):
        #字典或列表最好不设置为默认参数进行传递，否则在传递数据时，解包数据会出现错误
        conditions = {} if conditions is None else conditions
        return self.proxies.count(conditions)
