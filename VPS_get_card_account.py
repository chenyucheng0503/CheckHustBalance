from flask import Flask, request
from libhustpass import login
import json
import re
import requests
import traceback

app = Flask(__name__)


@app.route('/get_account', methods=['POST'])
def get_username_json():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
    else:
        return '<h1>只接受post请求！</h1>'
    username = dict1['username']
    password = dict1['password']
    return get_account(username, password)


def get_account(username, password):
    try:
        ticket = login(username, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
        r = requests.session()
        ret = r.get(ticket)
        account = re.findaz`ll('<span class="red">(.*)</span></span>', ret.text)[0]
        in_account = re.findall('<dd>(.*)元</dd>', ret.text)
        result = "当前余额为" + account + "<br></br>" + "当前过渡余额为" + in_account + "元 (不包括在余额中，食堂刷卡后增加)"
        return result
    except Exception as e:
        print(e)
        return "出现未知错误"