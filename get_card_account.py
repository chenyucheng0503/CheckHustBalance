from libhustpass import login
import json
import re
import requests
import traceback

# ticket = login("U201716052", "linjingyux3253,,", "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
#
# # now copy ticket to browser is ok
# # or open a new session
#
# r = requests.session()
# ret = r.get(ticket)
#
# # now do whatever you want
# account = re.findall('<span class="red">(.*)</span></span>', ret.text)[0]
# print(account)
#
# rc = r.get("http://ecard.m.hust.edu.cn/wechat-web/ChZhController/ChongZhi.html?value=10,033118&cardno=208030&acctype=1")
# print(rc.text)


def get_account(username, password):
    try:
        ticket = login(username, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
        r = requests.session()
        ret = r.get(ticket)
        account = re.findall('<span class="red">(.*)</span></span>', ret.text)[0]
        print("当前余额为" + account)
    except Exception as e:
        print(e)
        print("出现未知错误")


def recharge(username, password, value, pwd, cardno, acctype):
    try:
        ticket = login(username, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
        r = requests.session()
        ret = r.get(ticket)
        account = re.findall('<span class="red">(.*)</span></span>', ret.text)[0]
        in_account = re.findall('<dd>(.*)元</dd>', ret.text)
        print("当前余额为" + account)
        print("当前过渡余额为" + in_account + "元 (不包括在余额中，食堂刷卡后增加)")

        recharge_get = r.get(
            "http://ecard.m.hust.edu.cn/wechat-web/ChZhController/ChongZhi.html?value="+ str(value) + "," + str(pwd) + "&cardno=" + str(cardno) + "&acctype=" + str(acctype))
    except Exception as e:
        print(e)
        pass


def recharge(username, password, value, pwd, cardno):
    try:
        ticket = login(username, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
        r = requests.session()
        ret = r.get(ticket)
        account = re.findall('<span class="red">(.*)</span></span>', ret.text)[0]
        in_account = re.findall('<dd>(.*)元</dd>', ret.text)[0]
        print("当前余额为" + account)
        print("当前过渡余额为" + in_account + "元 (不包括在余额中，食堂刷卡后增加)")

        recharge_url = "http://ecard.m.hust.edu.cn/wechat-web/ChZhController/ChongZhi.html?value=" + str(value) + "," + str(pwd) + "&cardno=" + str(cardno) + "&acctype=1"
        recharge_get = r.get(recharge_url).text.strip("callJson(").strip(" )")
        recharge_json = json.loads(recharge_get)
        if recharge_json['errmsg']:
            print(recharge_json['errmsg'])
    except Exception as e:
        print(traceback.print_exc())
        pass


# get_account('U201716052', 'linjingyux3253,,')
recharge('U201716052', 'linjingyux3253,,', '1', '033118', '208030')