# 作者：沈圣海
# 本脚本仅供交流讨论，请勿用作商业用途
from selenium import webdriver
from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
options = EdgeOptions() 
options.use_chromium = True
options.add_argument('--user-agent=android')
# options.add_argument('--headless')   你们
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
i=270
while i<=299:
	num="201900700"+str(i)
	password="whsdu@"+num
	driver = Edge(options=options,executable_path ="E:\\E\\msedgedriver.exe")
	driver.get("https://xsc-health.wh.sdu.edu.cn/mobile/index.html#/common/office/fightncp/home")
	sleep(2)
	input_first=driver.find_element_by_xpath('//*[@id="root"]/div/form/div[1]/div[2]/div/input')
	input_first.click()
	input_first.send_keys(num)
	# pyautogui.typewrite(num)
	input2=driver.find_element_by_xpath('//*[@id="root"]/div/form/div[2]/div[2]/div/input')
	input2.click()
	input2.send_keys(password)
	# pyautogui.typewrite(password)
	input3=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/button')
	input3.click()
	sleep(1.5)
	input4=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div')
	input4.click()
	t=(By.XPATH ,'//*[@id="root"]/div/div/div[2]/button')
	sleep(2)
	element = WebDriverWait(driver, 800,0.01).until(EC.presence_of_element_located(t))
	# element2=WebDriverWait(driver, 800,1).until(EC.element_to_be_clickable(t))
	sleep(1)
	element.send_keys("\n")
	sleep(1.5)
	driver.close()
	print(i)
	i=i+1
print("好起来了")
