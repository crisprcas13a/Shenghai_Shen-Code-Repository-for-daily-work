# conding: utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
import glob
import os

# http://npm.taobao.org/mirrors/chromedriver/
driver = webdriver.Edge(executable_path ="D:\\Edgedriver\\msedgedriver")
driver.implicitly_wait(10)

LPSN = 'https://lpsn.dsmz.de/species?page='
pageList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for page in pageList:
    lspnURL = LPSN + page 
    driver.get(lspnURL)
    sleep(8)
    driver.find_element_by_xpath('//*[@id="main_taxon_list"]/div[4]/span[1]').click()
    sleep(5)
    # driver.find_element_by_xpath('//*[@id="main_taxon_list"]/h1').click()
    pyautogui.click(400, 300, button='left')
    sleep(0.5)
    pyautogui.hotkey('ctrl', 's')
    sleep(1)
    pyautogui.typewrite("LPSNspeciesPage_"+page)
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(5)
    

