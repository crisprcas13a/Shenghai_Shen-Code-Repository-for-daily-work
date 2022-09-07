from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Edge("D:\\Edgedriver\\msedgedriver")
driver.get('https://www.ezbiocloud.net/16SrRNA_list?tn=Root')
sleep(1)
s=1
def getTaxonomy_Accession(driver):
	r3=driver.find_elements_by_class_name("dt-head-center")	
	r2=driver.find_elements_by_class_name("dt-center")
	i,q=5,1
	while i <42:
		open("Accession_and_Taxonomy.txt",'a').write(r2[i].text.replace('\r', ' '))
		i+=4
		open("Accession_and_Taxonomy.txt",'a').write('\t'+r3[q].text.strip('\n') + '\n')
		q+=1
while True:
	getTaxonomy_Accession(driver)
	sleep(1)
	t1 = (By.XPATH ,'//*[@id="ssulist_next"]/a/i')
	element  =  WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(t1) )
	driver.find_element_by_xpath('//*[@id="ssulist_next"]/a/i').click()
	print('Page'+str(s)+':Done')
	s+=1








































# i,q=1,1
# def job(i):
#     t=(By.XPATH ,'//*[@id="ssulist"]/tbody/tr[' + str(i) +']/td[1]/button')
#     element = WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(t) )
#     get1=driver.find_element_by_xpath('//*[@id="ssulist"]/tbody/tr[' + str(i) +']/td[1]/button')
#     get1.click()
#     sleep(1)
#     r1=driver.find_element_by_xpath('//*[@id="seqImg"]')
#     seq=r1.get_attribute('data-clipboard-text')
#     r2=driver.find_element_by_xpath('//*[@id="16SrRNAResultView"]/div/div/div[6]')
#     title=driver.find_element_by_xpath('//*[@id="16SrRNAResultView"]/div/div/div[1]')
#     add=title.text.split(' ')[0]
#     text=r2.text
#     text1='\n'+add+"\n"+text
#     f1=open ('Taxonomy.txt','a')
#     f2=open ('Sequence.txt','a')
#     f1.write(text1)
#     f2.write('\n'+seq)
#     print(add,': done')
#     f1.close()
#     f2.close()
#     driver.get('https://www.ezbiocloud.net/16SrRNA_list?tn=Root')
# while q <= 500:
#     judge=i%10
#     if judge !=0:
#         job(i)
#         i+=1
#     else:
#         job(i)
#         sleep(1)
#         t1=(By.XPATH ,'//*[@id="ssulist_next"]/a/i')
#         element = WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(t1) )
#         driver.find_element_by_xpath('//*[@id="ssulist_next"]/a/i').click()
#         sleep(1)
#         i-=9
#     q+=1    
        

    




















