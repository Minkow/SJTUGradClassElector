from selenium import webdriver
from time import sleep
import requests
import pytesseract
from PIL import Image
import random


options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('http://yjsxk.sjtu.edu.cn/yjsxkapp/sys/xsxkapp/index.html')
sleep(2)
jump = browser.find_elements_by_tag_name('button')
jump[-1].click()

captcha_url = "https://jaccount.sjtu.edu.cn/jaccount/captcha"
user = 'yours'
pswd = 'yours'


def get_captcha(captcha_url, cookies, params):
    response = requests.get(captcha_url, cookies=cookies, params=params)
    with open('img.jpeg', 'wb+') as f:
        f.writelines(response)

try:
    cookies = browser.get_cookies()
    cookies = {i["name"]: i["value"] for i in cookies}
    uuid = browser.find_element_by_xpath('//form/input[@name="uuid"]')
    params = {
        'uuid': uuid.get_attribute('value')
    }
    get_captcha(captcha_url, cookies, params)
    image = Image.open('img.jpeg')
    code = pytesseract.image_to_string(image)
    code = code.replace(' ','').replace('|','l')
    print(code)
    input_user = browser.find_element_by_id('user')
    input_user.send_keys(user)
    input_pass = browser.find_element_by_id('pass')
    input_pass.send_keys(pswd)
    input_code = browser.find_element_by_id('captcha')
    input_code.send_keys(code)
    print(browser.current_url)
finally:
    print('success!')

browser.get('http://yjsxk.sjtu.edu.cn/yjsxkapp/sys/xsxkapp/course.html')
sleep(0.5)
xk = browser.find_elements_by_tag_name('a')
cnt=0
while(1):
    for item in xk:
        if str(item.text) == '选课':
            item.click()
            rtime1 = random.random() / 2
            sleep(0.5 + rtime1)
            yon = browser.find_elements_by_tag_name('button')
            yon[0].click()
            rtime2 = random.random() / 2
            sleep(0.5 + rtime2)
            confirm = browser.find_elements_by_tag_name('button')
            confirm[0].click()
            rtime3 = random.random() * 5
            sleep(5 + rtime3)
    cnt += 1
    print(cnt)
    rtime4 = random.random() * 30
    sleep(30 + rtime4)
