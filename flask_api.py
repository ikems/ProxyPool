"""
部署爬虫在本地，并提供一个简单稳定的接口，去获取ip
"""


import flask
from save_to_db import SaveDB
import json


app = flask.Flask(__name__)


#抓取一个ip
@app.route('/one_proxy')
def get_one():
    return json.dumps(SaveDB().get_proxy(1))


#抓取多个ip
@app.route('/many_proxy')
def get_many():
    #向url提供一个参数，传递需要几个代理ip
    args = flask.request.args
    return json.dumps(SaveDB().get_proxy(args['num']))


#删除
@app.route('/delete')
def delete():
    args = flask.request.args
    try:
        SaveDB().delete_proxy(args)
        return f'删除成功：{args}'
    except Exception:
        return f'删除失败：{args}'


def api_run():
    app.run()


# if __name__ == '__main__':
#     api_run()
