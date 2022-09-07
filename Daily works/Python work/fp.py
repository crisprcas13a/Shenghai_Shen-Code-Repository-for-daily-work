from typing import Text
from urllib import request
from bs4 import BeautifulSoup


for i in range(1,101):
    url="https://www.runoob.com/python/python-exercise-example"+str(i)+".html"
    print(url)
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup_text = soup.find('div',id="content",class_="article-intro").text
    w=open('fp.txt','a',encoding="utf-8")
    w.write(soup_text)
    w.write('---------------------------------------------------------')
    w.close()
    
    
    
    
    