import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

import time
import re, math

from fake_useragent import UserAgent
# from random import randrange
ua = UserAgent()
ua = ua.random

import requests
from bs4 import BeautifulSoup
import lxml

import xml.etree.ElementTree as xml

import json
import csv
import pandas as pd
# df = pd.read_csv('data.csv', sep=';', header=0)

url = 'https://opensea.io/rankings?sortBy=one_day_volume'


print('start...')

# # 1
# #
# options = webdriver.FirefoxOptions()
# options.set_preference("general.useragent.override", f"{ua}")
#
# s = Service('geckodriver.exe')
#
# driver = webdriver.Firefox(service=s, options=options)
#
# driver.implicitly_wait(1.5)
# hhh = driver.get(url)
# # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#
# time.sleep(3)
# source_html = driver.page_source
#
# time.sleep(2)
# driver.close()
# driver.quit()
# #
# # #
# # # with requests.Session() as session:
# # #     response = session.get(url=url, headers=headers)
# # #
# # # # запись СПАРСЕНОЙ инфы в ХТМЛ-файл
# # with open('index.html', 'w', encoding='utf-8') as file:
# #     file.write(source_html)
#
# # # 2
# # #
# # #soup = BeautifulSoup(html, 'lxml')
# #
# # with open("index.html", "r", encoding='utf-8') as f:
# #     source_html = f.read()
# #
# soup = BeautifulSoup(source_html, 'lxml')
#
#
# """
# в коде страницы есть скрипт:
# <script id="__NEXT_DATA__" ... </scrypt>
#
# в этом скрипте между тегами:
# "json": и "data: лежит готовый JSON с данными!!!
#
# ...достаём его:
# """
# script_all = soup.find('script', id='__NEXT_DATA__')
# script_ = str(re.findall('\"json\"\:\{\"data\"(.*?)\"data\"\:', str(script_all))).\
#                                                                 replace(",']", "").\
#                                                                 replace("['", "").\
#                                                                 replace('\\\\"', "'")
# json_all = '{"data"'+script_
# #scr1 = '{"data"'+ (str(re.findall('\"json\"\:\{\"data\"(.*?)\"data\"\:', str(script))).replace(",']", "").replace("['", ""))
#
# with open('_my_json.json.', 'w', encoding='utf-8') as file:
#     #json.dump(json_all, file, indent=4, ensure_ascii=False)
#     file.write(json_all)

# 3
#
with open("_my_json.json", "r") as read_file:
    data_ = json.load(read_file)
#dict_obj = json.loads('_my_json.json')
for aaa in range(0, 2):
    print(data_['data']['rankings']['edges'][aaa]['node']['name'])
    print(data_['data']['rankings']['edges'][aaa]['node']['statsV2']['oneDayVolume']['unit'])