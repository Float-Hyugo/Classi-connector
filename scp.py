from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from plyer import notification
from selenium.webdriver.chrome.options import Options
# classi 用LINE Botの作成

options = Options()
options.add_argument('--headless')

driver = None

#memo 新規通知class ng-binding bold
#memo 既読済みclass ng-binding

def login():
    global driver
    driver = webdriver.Chrome(r'C:\Users\name\chromedriver',options=options)
    driver.get('https://auth.classi.jp/students')
    USER_NAME = ""
    PASSWORD = ""
    id_text = driver.find_element_by_name("classi_id")
    password_text = driver.find_element_by_name("password")

    id_text.send_keys(USER_NAME)
    password_text.send_keys(PASSWORD)
    login_btn = driver.find_element_by_name("button")

    login_btn.click()

def open_msg():
    global driver
    login()
    msg_tab = driver.find_element_by_xpath('/html/body/div[1]/div/article/div/section[2]/ul/li[10]/a')
    msg_tab.click()

    time.sleep(2)



def send_msg(t_name:str,content:str):
    global driver
    teacher = t_name + " 先生"
    print(teacher)
    open_msg()
    search = None
    teacher_list = [t.find_element_by_xpath('div/div[1]/p[1]/span') for t in driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/article/div[2]/div[1]/ul/li')]
    for l in teacher_list:
        print(l.text)
        if l.text == teacher:
            search = l
    search.click()

    time.sleep(1)

    text = driver.find_element_by_id("message-send-area")
    text.send_keys(content)

    send_b = driver.find_element_by_id("message-send-button")
    send_b.click()

    time.sleep(2)

    check_b = driver.find_element_by_xpath('/html/body/div[9]/div/div/div[1]/div[3]/button[2]')
    check_b.click()
    time.sleep(2)
    driver.close()

def has_messages():
    try:
        global driver
        res = dict()
        open_msg()
        friend_list = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/article/div[2]/div[1]/ul/li/div/span[@class="badge bg-color-red ng-binding"]/parent::node()')
        for f in friend_list:
            x = f.find_element_by_xpath('div[1]/p[1]/span')
            res[x] = ""
            print(x.text)
        print('fin')
        if len(friend_list) == 0:
            driver.close()
            return None
        for fr in friend_list:
            x = fr.find_element_by_xpath('div[1]/p[1]/span')
            msg = list()
            ct_e = fr.find_element_by_xpath('span[@class="badge bg-color-red ng-binding"]')
            ct = int(ct_e.text)
            fr.click()
            time.sleep(0.5)
            m = len(driver.find_elements_by_xpath('//*[@id="message-list"]/div'))
            for c in range(ct-1,-1,-1):
                last = driver.find_element_by_xpath(f'//div[@class="chatContainer pull-right"]/div[@id="message-list"]/div[{m - c}]')
                ms = last.find_element_by_xpath('div[2]/div[1]/p')
                mst = ms.text
                msg.append(mst)
            name = x.text
            name = name[:-3]
            res[name] = msg
        driver.close()
        time.sleep(0.1)
        return res

            
            

    except Exception as e:
        print(e)
        driver.close()
        return

print(has_messages())



    