from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
path='C:\\Users\\lenovo\\Desktop\\ru.html'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup=BeautifulSoup(htmlhandle,'lxml')
sps=soup.find_all(attrs={'id':"dataList"})
rr=0
for i in sps:
	q=i.text.splitlines()
	we=[6]
	m=0
	n=0
	# i=23
	# w=0
	# while i <=23+15*74:
	# 	w+=float(q[i])
	# 	i+=15
	for t in q:
		if t == str('必修'):
			m += 1
			if m >=2:
				we.append(q[n-3])
		n+=1
for ee in we :
	rr+=float(ee)
print(rr)
			# print(t)
			# w=q[e-3]
			# print(w)	


