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
