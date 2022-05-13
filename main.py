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

import xlsxwriter
import shutil

workbook = xlsxwriter.Workbook('test1.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True, 'font_color': 'red'})
bold.set_align('center')

bold_1 = workbook.add_format({'bold': True, 'font_color': 'black'})
bold_1.set_align('center')

bold_2 = workbook.add_format({'bold': True, 'font_color': 'blue'})
bold_2.set_align('center')

bold_3 = workbook.add_format({'bold': True, 'font_color': 'black'})
bold_3 = workbook.add_format({'bg_color': '#b4b4b4'})
bold_3.set_align('center')

data_format1 = workbook.add_format({'bg_color': '#b4b4b4'})
data_format1.set_align('center')
#
# =========================================================

# Format the first column
worksheet.set_column('A:A', 25, data_format1)
worksheet.set_column('B:B', 40)
worksheet.set_column('C:H', 25)

worksheet.set_default_row(25)

worksheet.write('A1', '', bold_3)
worksheet.write('B1', 'Collection', bold_1)
worksheet.write('C1', 'Volume', bold_1)
worksheet.write('D1', '24h %', bold_1)
worksheet.write('E1', '7d %', bold_1)
worksheet.write('F1', 'Floor Price', bold_1)
worksheet.write('G1', 'Num Owners', bold_1)
worksheet.write('H1', 'Items', bold_1)



url = 'https://opensea.io/rankings?sortBy=one_day_volume'


print('start...')

# 1
#
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", f"{ua}")

s = Service('geckodriver.exe')

driver = webdriver.Firefox(service=s, options=options)

driver.implicitly_wait(1.5)
hhh = driver.get(url)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(3)
source_html = driver.page_source

time.sleep(2)
driver.close()
driver.quit()
#
# #
# # with requests.Session() as session:
# #     response = session.get(url=url, headers=headers)
# #
# # # запись СПАРСЕНОЙ инфы в ХТМЛ-файл
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(source_html)

# # # 2
# # #
# # #soup = BeautifulSoup(html, 'lxml')
# #
# with open("index.html", "r", encoding='utf-8') as f:
#     source_html = f.read()
# # #
soup = BeautifulSoup(source_html, 'lxml')

# lot_img_url = soup.find('picture').find('img', class_='Image lazyload').get('data-src')
# res = requests.get(lot_img_url, stream=True)
# file_name = f'{lot_num.replace(" ", "")}.jpg'
# with open(file_name, 'wb') as f:
#     shutil.copyfileobj(res.raw, f)

# lot_url = soup.find_all('a', class_='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0')
# print(len(lot_url))
# for i in lot_url:
#     pass
#     #print(lot_url.get('href'))
# breakpoint()



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
script_all = soup.find('script', id='__NEXT_DATA__')
script_ = str(re.findall('\"json\"\:\{\"data\"(.*?)\"data\"\:', str(script_all))).\
                                                                replace(",']", "").\
                                                                replace("['", "").\
                                                                replace('\\\\"', "'")
json_all = '{"data"'+script_
#scr1 = '{"data"'+ (str(re.findall('\"json\"\:\{\"data\"(.*?)\"data\"\:', str(script))).replace(",']", "").replace("['", ""))

with open('_my_json.json.', 'w', encoding='utf-8') as file:
    #json.dump(json_all, file, indent=4, ensure_ascii=False)
    file.write(json_all)

# 3
#
with open("_my_json.json", "r") as read_file:
    data_ = json.load(read_file)

row = 2
for aaa in range(0, 100):
    print(aaa)
    img_url = f"{data_['data']['rankings']['edges'][aaa]['node']['logo']}"
    collection = f"{data_['data']['rankings']['edges'][aaa]['node']['name']}"
    volume = f"{data_['data']['rankings']['edges'][aaa]['node']['statsV2']['oneDayVolume']['unit']}"
    d24h_ = f"{data_['data']['rankings']['edges'][aaa]['node']['statsV2']['oneDayChange']}"
    d7d = f"{data_['data']['rankings']['edges'][aaa]['node']['statsV2']['sevenDayChange']}"
    try:
        floor_price = f"{data_['data']['rankings']['edges'][aaa]['node']['statsV2']['floorPrice']['eth']}"
    except:
        floor_price = 'None'
    num_owners = f"{data_['data']['rankings']['edges'][aaa]['node']['statsV2']['numOwners']}"
    items = f"{data_['data']['rankings']['edges'][aaa]['node']['statsV2']['totalSupply']}"

    res = requests.get(img_url, stream=True)
    file_name = f'./img/{aaa}.jpg'
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(res.raw, f)

    worksheet.insert_image(f'A{row}', file_name, {'x_scale': 0.25, 'y_scale': 0.25, 'x_offset': 10})
    worksheet.write(f'B{row}', collection, bold_2) # worksheet.write_url(f'F{row}', url, string=f'{lot_num}')
    worksheet.write(f'C{row}', volume)
    worksheet.write(f'D{row}', d24h_)
    worksheet.write(f'E{row}', d7d)
    worksheet.write(f'F{row}', floor_price)
    worksheet.write(f'G{row}', num_owners)
    worksheet.write(f'H{row}', items)

    row = row + 1

workbook.close()
