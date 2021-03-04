from selenium import webdriver
from selenium.webdriver import ChromeOptions()
import time
import os

os.environ["USER_ID"] = ""
os.environ["PASS"] = ""

#バックグラウンドでブラウザを起動するオプション
option = ChormeOptions()
options.add_argument('--headless')

class Scraping():
  def __init__(self):
    self.driver = None
  
  def login(self):
    self.driver = webdriver.Chrome('path to driverexe',options=options)
    self.driver.get('https://auth.classi.jp/students')
    id = self.driver.find_element_by_name('classi_id')
    password = self.driver.find_element_by_name('password')
    
    id.send_keys(os.environ["USER_ID"])
    password.send_keys(os.environ["PASS"])
    
    login_btn = self.driver.find_element_by_name('button')
    
