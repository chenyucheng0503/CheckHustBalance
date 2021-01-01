import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from libhustpass import main
import traceback

def get_account(account, password):
    ticket = main.doLogin(account, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    try:
        driver.get(ticket)
    except Exception:
        print("gg")
    try:
        print(driver.find_element_by_xpath('//div[@class="wrapper"]/section/dl[2]/dd/div/span[@class="red"]').text)
    except:
        print("出现未知错误")
    finally:
        driver.quit()


def recharge(account, password, amount, pwd):
    try:
        ticket = main.doLogin(account, password, "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
        driver.get(ticket)
        print("当前余额：" + driver.find_element_by_xpath('//div[@class="wrapper"]/section/dl[2]/dd/div/span').text)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'aqita')))
        except TimeoutException:
            print('第一次尝试失败')
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'aqita')))
        driver.find_element_by_id('aqita').click()
        time.sleep(0.5)
        driver.find_element_by_id('value').send_keys(str(amount))
        time.sleep(1)
        driver.find_element_by_id('pwd').send_keys(str(pwd))
        time.sleep(1)
        qrcz = driver.find_element_by_id('qrcz')
        webdriver.ActionChains(driver).move_to_element(qrcz).click(qrcz).perform()

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        time.sleep(0.5)
        alter = driver.switch_to.alert
        print(alter.text)
        alter.accept()
    except:
        traceback.print_exc()
        print("出现未知错误")
    finally:
        driver.quit()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False,
        },
        "download": {
            'default_directory': "/usr/local/download",
        }
    })
    driver = webdriver.Chrome(options=options)

    # get_account('U201716052', 'linjingyux3253,,')
    recharge('U201716052', 'linjingyux3253,,', 1, '033118')
