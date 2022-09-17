
from Bio import SeqIO
from selenium import webdriver
import re, time
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
options = EdgeOptions() 
options.use_chromium = True
# json, sys
st = time.time()
input_file = "E://ZFP.txt"
out_file = "E://ZFProt6.txt"
expasy = Edge(options=options,executable_path ="D:\\Programs\\DangoTranslator\\app\config\\tools\\msedgedriver.exe")
expasy.get("https://web.expasy.org/protparam/")
class expasy_cal():
    '''get physical and chemical parameters for a given protein sequence file
        based on web https://web.expasy.org/protparam/'''
    def inputseq(seq):
        """input the protein sequence"""
        if expasy.find_element_by_xpath('//*[@id="sib_body"]/form/textarea').is_displayed():
            expasy.find_element_by_xpath('//*[@id="sib_body"]/form/p[1]/input[1]').click() 
            expasy.find_element_by_xpath('//*[@id="sib_body"]/form/textarea').send_keys(seq)
            expasy.find_element_by_xpath('//*[@id="sib_body"]/form/p[1]/input[2]').click()
        else:
            print("input box is not displayed")
    def compute():
        """get the parameters showed below"""
        time.sleep(0.3)  
        while True:
            if expasy.find_element_by_xpath('//*[@id="sib_body"]/h2').is_displayed():
                pd = {}
                parameters = expasy.find_element_by_xpath('//*[@id="sib_body"]/pre[2]').text.split("\n\n")  
                aaa = '\n'.join(parameters)
                bbb = re.split("[:\n]", aaa)  
                pd["number_of_amine_acid"] = bbb[1].strip()
                pd["molecular_weight"] = bbb[3].strip()
                pd["theoretical_pi"] = bbb[5].strip()
                pd["instability_index"] = re.findall("[\d.]+", bbb[66])[0] 
                pd["aliphatic_index"] = bbb[70].strip()
                pd["gravy"] = bbb[72].strip()
                return pd
                break
            else:
                print("loading")

with open(out_file, "w", encoding='utf-8') as f:
    f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
        'seq_id',
        'number_of_amine_acid',
        'molecular_weight',
        'theoretical_pi',
        'instability_index',
        'aliphatic_index',
        'gravy'))
    pros = SeqIO.parse(input_file, "fasta")
    i = 0
    for pro in pros:
        print("=" * 10, "seq", i + 1, "->", pro.id, "on the way", "=" * 10)
        expasy_cal.inputseq(seq=pro.seq)
        cccc = expasy_cal.compute()
        number_of_amine_acid = cccc['number_of_amine_acid']
        molecular_weight = cccc['molecular_weight']
        theoretical_pi = cccc['theoretical_pi']
        instability_index = cccc['instability_index']
        aliphatic_index = cccc['aliphatic_index']
        gravy = cccc['gravy']
        f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
            pro.id,
            number_of_amine_acid,
            molecular_weight,
            theoretical_pi,
            instability_index,
            aliphatic_index,
            gravy))
        i += 1
        expasy.back() 
expasy.close()
et = time.time()
print("process finished")
print("taking time", et - st, "s")