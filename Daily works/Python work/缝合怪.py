from bs4 import BeautifulSoup
path='C:\\Users\\lenovo\\Desktop\\Sublime\\学长的任务罢了\\test.html'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup=BeautifulSoup(htmlhandle,'lxml')
taxTreeOpens = soup.find_all('div', {'class':'tax-tree open'})
for tax in taxTreeOpens:
	rawLine = tax.text.replace('"', '').split('\n')[1:]
	newLine = '\t'.join(rawLine) + '\n'
	print(newLine)







