# conding: utf-8

from bs4 import BeautifulSoup
import os

def getInforLine(LPSNfile):
    summaryLPSN = []
    html = open(LPSNfile, 'rb').read()
    soup = BeautifulSoup(html, 'html.parser')
    taxTreeOpens = soup.find_all('div', {'class':'tax-tree open'})
    for tax in taxTreeOpens:
        print(tax)
        rawLine = tax.text.replace('"', '').split('\n')[1:]
        # print(len(rawLine))
        newLine = '\t'.join(rawLine) + '\n'
        summaryLPSN.append(newLine)
    return summaryLPSN

files = [ fn for fn in os.listdir('HTMLs') if '.html' in fn]
for fn in files:
    LPSNfile = 'HTMLs/' + fn
    taxInfor = getInforLine(LPSNfile)
    open('SummaryLPSN.txt', 'a').writelines(taxInfor)
    print(LPSNfile)
print('-----------------------------DONE-----------------------------')