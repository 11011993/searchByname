import os 
import random
import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException




driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('https://www.linkedin.com/uas/login')
files = open('config.txt')
lines = files.readlines()
username = lines[0]
password = lines[1]
elementID = driver.find_element_by_id('username')
elementID.send_keys(username)
elementID = driver.find_element_by_id('password')
elementID.send_keys(password)
elementID.click()
m = 'https://www.linkedin.com/search/results/all/?keywords=dewan%20singh%20parmar&origin=GLOBAL_SEARCH_HEADER'
#elementID.submit()
driver.getText(m)