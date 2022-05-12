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

