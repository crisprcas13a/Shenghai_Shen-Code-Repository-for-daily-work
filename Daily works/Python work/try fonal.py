from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
i,q,z=1,1,1 
driver = webdriver.Edge("E:\\E\\msedgedriver.exe")
driver.get('https://www.ezbiocloud.net/16SrRNA_list?tn=Root')
def Accession(i):
    t=(By.XPATH ,'//*[@id="ssulist"]/tbody/tr[' + str(i) +']/td[1]/button')
    WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(t) )
    get1=driver.find_element_by_xpath('//*[@id="ssulist"]/tbody/tr[' + str(i) +']/td[1]/button')
    get1.click()
    sleep(1)
    r1=driver.find_element_by_xpath('//*[@id="seqImg"]')
    seq=r1.get_attribute('data-clipboard-text').splitlines()
    wewant=(driver.find_element_by_xpath('//*[@id="16SrRNAResultView"]/div/div/div[1]').text).split(" ")[0]
    seq[0]='>'+wewant
    test="\n".join(seq)
    f2=open ('SEQ.txt','a')
    f2.write('\n'+test)
    f2.close()
    driver.back()
    print(wewant)
while q <= 500:
    judge=i%10
    if judge !=0:
        Accession(i)
        i+=1
    else:
        z+=1
        Accession(i)
        sleep(1)
        t1=(By.XPATH ,'//*[@id="ssulist_next"]/a/i')
        WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(t1) )
        driver.find_element_by_xpath('//*[@id="ssulist_next"]/a').click()
        sleep(1)
        i-=9
        print(z)
    q+=1    
    


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# i,q,z=1,1,1 
# driver = webdriver.Edge("E:\\E\\msedgedriver.exe")
# driver.get('https://www.ezbiocloud.net/16SrRNA_list?tn=Root')
# while True:
#     t1=(By.XPATH ,'//*[@id="ssulist_next"]/a/i')
#     element = WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(t1) )
#     driver.find_element_by_xpath('//*[@id="ssulist_next"]/a').click()


import numpy 
a = numpy.arange(1,6,1)
print(a)