from bs4 import BeautifulSoup
import requests
import re
f=open('rs.txt','r')
def getq(q):
	website='https://lpsn.dsmz.de/species/'+q
	websites=requests.get(website).text
	soup=BeautifulSoup(websites,'lxml')
	e=soup.find(attrs={'class':'black fasta-download'})
	target=e.attrs['href']
	if target!=None:
		c='https://lpsn.dsmz.de'+target
		w2=requests.get(c).content
		w2=w2.decode('utf-8')
		p=re.compile('/s')
		w3=p.sub('',w2)
		file=open('fastaall.txt','a')
		file.write(w3)
		file.close()
	else:
		file=open('fastaall.txt','a')
		file.write(q+'找不到相关fasta')
		file.close()
for i in f.readlines():
	# q=i.replace('','-')
	m=i.split()
	str='-'
	q=str.join(m)
	getq(q)
print("----------------------------------------------------------finished----------------------------------------------------------------------")




	
	