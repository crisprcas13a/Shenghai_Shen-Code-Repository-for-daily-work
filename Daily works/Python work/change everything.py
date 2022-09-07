import re
import pandas as pd
count={}
def dic_to_csv(dic_data,name):
    pd.DataFrame(dic_data,index=[0]).to_csv('{}.csv'.format(name))
def deal(line):
    global count
    after=line.split(',')
    if after[1]!=""and after[1]!='地市':
            key=after[1]
            if key in count:
                value=int(count[key])
                value+=1
                count[key]=str(value)
            else:
                count[key]='1'
names=['reds',"greens",'blues']
for name in names:
    path="C:\\Users\\Zz\\Desktop\\2018{}.txt".format(name)
    f=open(path,'r')
    lines=f.readlines()
    for line in lines :
        deal(line)
    f.close()
    dic_to_csv(count,name)
    


















