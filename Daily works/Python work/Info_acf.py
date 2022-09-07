# 作者：沈圣海
# 本脚本仅供交流讨论，请勿用作商业用途
from selenium import webdriver
from time import sleep
import pyautogui
from msedge.selenium_tools import Edge, EdgeOptions
import pyperclip
options = EdgeOptions()
options.use_chromium = True
options.add_argument('--user-agent=android')
i=1
while i<=299:
	if i<10:
		num="20190070000"+str(i)
	elif i>=10 and i<100:
		num="2019007000"+str(i)
	else:
		num="201900700"+str(i)
	password="whsdu@"+num
	driver = Edge(options=options,executable_path ="D:\\Edgedriver\\msedgedriver")
	driver.get("https://xsc-health.wh.sdu.edu.cn/mobile/index.html#/common/office/fightncp/home")
	sleep(1)
	input_first=driver.find_element_by_xpath('//*[@id="root"]/div/form/div[1]/div[2]/div/input')
	input_first.click()
	pyautogui.typewrite(num)
	input2=driver.find_element_by_xpath('//*[@id="root"]/div/form/div[2]/div[2]/div/input')
	input2.click()
	pyautogui.typewrite(password)
	input3=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/button')
	input3.click()
	sleep(1)
	input4=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div')
	input4.click()
	sleep(2)
	input5=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/button')
	sleep(1)
	input5.click()
	sleep(1)
	driver.close()
	i=i+1
print("好起来了")