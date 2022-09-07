import requests
from lxml import etree
 
requests.urllib3.disable_warnings()
 
try:
    url = 'http://news.cyol.com/node_67071.htm'
    response = requests.get(url,verify=False) 
    html = etree.HTML(response.text)
    newest = html.xpath('/html/body/div[@class="mianbody"]/dl[@class="listMM"]/dd[@class="picB"]/ul[@class="movie-list"]/li[1]/a/@href')[0]
    img_path = newest.replace('m.html','images/end.jpg').replace('index.html','images/end.jpg')
    
except: print('Bad Requests')
 
 
with open('end.jpg','wb') as f:
    img = requests.get(img_path)
    f.write(img.content)
    f.close()
    print('Saved!')
    