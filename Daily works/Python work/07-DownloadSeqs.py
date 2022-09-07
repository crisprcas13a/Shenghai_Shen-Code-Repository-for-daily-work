# conding: utf-8

from bs4 import BeautifulSoup
import requests
from time import sleep
import re

def getSeqs(seqURL):
	print('--seqURL',seqURL)
	seqHtml = requests.get(seqURL)
	if int(seqHtml.status_code) == 200:
		sequence = seqHtml.text.replace('\r', '').strip()
		header = '_'.join(sequence.split('\n')[0].split('_')[:2])
		seq = sequence.split('\n')[1] + '\n'
		return header + '\n' + seq
	else:
		return '-- NoSeqs --'

def getSeqsUrl(speciesHtml):
	if 'black fasta-download' in str(speciesHtml.text):
		soup = BeautifulSoup(speciesHtml.text, 'html.parser')
		if soup.find_all('a', {'class': 'black fasta-download'})[0].text == 'FASTA ':
			seqURL = 'https://lpsn.dsmz.de' + soup.find_all('a', {'class': 'black fasta-download'})[0].get('href')
			# print('check lenth seqURL:', len(seqURL))
			return seqURL
		else:
			return '-- No Seqs --'

startNum = 0
speciesList = [line.strip() for line in open('DownloadSpeciesList.txt').readlines()]
# open('DownloadSpeciesSeqs.fasta', 'w')
for spe in speciesList[startNum:]:
	speURl = 'https://lpsn.dsmz.de/species/' + spe.replace(' ', '-')
	print('-- Species URL:', speURl)
	speciesHtml = requests.get(speURl)
	if int(speciesHtml.status_code) == 200:
		seqURL = getSeqsUrl(speciesHtml)
		if seqURL != '-- No Seqs --' and seqURL != None:
			print('-- Ongoing', spe, '--')
			seqs = getSeqs(seqURL)
			if seqs != '-- NoSeqs --':
				open('DownloadSpeciesSeqs.fasta', 'a').write(seqs)
				print('-- Done', spe, '--', speciesList.index(spe) + 1, '--')
				sleep(1)

print('-----------------------------DONE-----------------------------')
