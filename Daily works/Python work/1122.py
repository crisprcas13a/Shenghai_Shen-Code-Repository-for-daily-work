from selenium import webdriver
from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions() 
options.use_chromium = True
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = Edge(options=options,executable_path ="D:\\Edgedriver\\msedgedriver")
driver.get('https://www.ezbiocloud.net/16SrRNA_list?tn=Root')