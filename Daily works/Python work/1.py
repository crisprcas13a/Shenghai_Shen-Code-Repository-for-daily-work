from selenium import webdriver
from time import sleep
import pyautogui
from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions()
options.use_chromium = True
options.add_argument('--user-agent=android')
i=231
while i<=298:
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
	sleep(1)
	input5=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/button')
	input5.click()
	sleep(1)
	driver.close()
	i=i+1


