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

options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", f"{ua}")

s = Service('geckodriver.exe')

driver = webdriver.Firefox(service=s, options=options)

driver.implicitly_wait(1.5)
hhh = driver.get(url)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(3)
html = driver.page_source

# with requests.Session() as session:
#     response = session.get(url=url, headers=headers)
#
# запись СПАРСЕНОЙ инфы в ХТМЛ-файл
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html)