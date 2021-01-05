import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium.libhustpass import main
from flask import Flask, request
import json
import traceback

app = Flask(__name__)


def start_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('prefs', {'credentials_enable_service': False, 'profile': {'password_manager_enabled': False,}, "download": {'default_directory': "/usr/local/download",}})
    driver = webdriver.Chrome(options=options)
    return driver


@app.route('/get_account', methods=['POST'])
def get_account_json():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
    else:
        return '<h1>只接受post请求！</h1>'
    account = dict1['account']
    password = dict1['password']
    result = get_account(account, password)
    return result


def get_account(account, password):
    driver = start_selenium()
    ticket = main.doLogin(account, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    try:
        driver.get(ticket)
    except:
        return "gg"
    try:
        balance = driver.find_element_by_xpath('//div[@class="wrapper"]/section/dl[2]/dd/div/span[@class="red"]').text
        print('n')
        return balance
    except:
        return "出现未知错误"
    finally:
        driver.quit()


@app.route('/recharge', methods=['POST'])
def get_recharge_json():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
    else:
        return '<h1>只接受post请求！</h1>'
    account = dict1['account']
    password = dict1['password']
    amount = dict1['amount']
    pwd = dict1['pwd']
    result = recharge(account, password, amount, pwd)
    return result


def recharge(account, password, amount, pwd):
    try:
        driver = start_selenium()
        ticket = main.doLogin(account, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
        driver.get(ticket)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'aqita')))
        except TimeoutException:
            print('第一次尝试失败')
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'aqita')))

        result_1 = "<h1>当前余额：" + driver.find_element_by_xpath('//div[@class="wrapper"]/section/dl[2]/dd/div/span').text + "</h1>"
        print(result_1)

        driver.find_element_by_id('aqita').click()
        time.sleep(0.5)
        driver.find_element_by_id('value').send_keys(str(amount))
        time.sleep(1)
        driver.find_element_by_id('pwd').send_keys(str(pwd))
        time.sleep(1)
        qrcz = driver.find_element_by_id('qrcz')
        webdriver.ActionChains(driver).move_to_element(qrcz).click(qrcz).perform()

        driver.execute_script("window.confirm = function(){return true;}");
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # time.sleep(0.5)
        # alter = driver.switch_to.alert
        # result_2 = "<h1>" + alter.text + "</h1>"
        # alter.accept()
        return result_1
    except:
        traceback.print_exc()
        return "出现未知错误"
    finally:
        driver.quit()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1037)
