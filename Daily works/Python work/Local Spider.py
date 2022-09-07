from bs4 import BeautifulSoup
import re
path='C:\\Users\\lenovo\\Desktop\\test.html'
# x='div class="tax-tree open"'
line1=re.compile(r'^[is]')
line2=re.compile(r'[i=]$')
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup=BeautifulSoup(htmlhandle,'lxml')
for i in soup.find_all(class_="tax-tree open"):
	i=str(i)
	i=re.sub('[<>/]', '', i)
	# print(str(i).split())
	for m in i.split("/n"):
		n=m.split('"')
		# print(n)
		for t in n :
			# if str(t).startswith('i') and str(t).endswith('i') or startswith('s') and endwith("="):
			if re.search(line1,t) and re.search(line2,t):
				t=t.strip("i")
				if not t.startswith("span"):
					print(t)
				# print(t.strip("i"),"哈哈哈")
				# print(t)
		
	













