import requests
import json
from bs4 import BeautifulSoup
url='https://www.ezbiocloud.net/16SrRNA_list?tn=Root'
header={'content-language': 'zh-CN',
'content-length': '2784',
'content-type': 'text/html; charset=UTF-8',
'date': 'Sun, 06 Dec 2020 07:40:14 GMT',
'server': 'nginx/1.9.12',
'set-cookie': 'AWSALB=e/JtITt9oLMpDyzvQfX0v0vwMNdPVQ7bZlaF4zzcCj+q/T/9QiYKajAKXWp6TWoZOlDvDb5bWv+hhybI1s5aFxd/vvqgOw3E4UEKnwZmiNMhomlq1+nmL6ikftnV; Expires=Sun, 13 Dec 2020 07:40:13 GMT; Path=/',
'set-cookie': 'AWSALBCORS=e/JtITt9oLMpDyzvQfX0v0vwMNdPVQ7bZlaF4zzcCj+q/T/9QiYKajAKXWp6TWoZOlDvDb5bWv+hhybI1s5aFxd/vvqgOw3E4UEKnwZmiNMhomlq1+nmL6ikftnV; Expires=Sun, 13 Dec 2020 07:40:13 GMT; Path=/; SameSite=None; Secure'}
Query_String_Parameters={'tn': 'Root',
'draw':'1',
'columns[0][data]': '0',
# 'columns[0][name]':'',
'columns[0][searchable]': 'true',
'columns[0][orderable]': 'true',
# 'columns[0][search][value]': ,
'columns[0][search][regex]': 'false',
'columns[1][data]': '1',
# 'columns[1][name]': ,
'columns[1][searchable]': 'true',
'columns[1][orderable]': 'true',
# 'columns[1][search][value]': ,
'columns[1][search][regex]': 'false',
'columns[2][data]': '2',
# 'columns[2][name]': ,
'columns[2][searchable]': 'true',
'columns[2][orderable]': 'true',
# 'columns[2][search][value]': ,
'columns[2][search][regex]': 'false',
'columns[3][data]': '3',
# 'columns[3][name]': ,
'columns[3][searchable]': 'true',
'columns[3][orderable]': 'true',
# 'columns[3][search][value]': ,
'columns[3][search][regex]': 'false',
'columns[4][data]': '4',
# 'columns[4][name]': ,
'columns[4][searchable]': 'true',
'columns[4][orderable]': 'true',
# 'columns[4][search][value]': ,
'columns[4][search][regex]': 'false',
'order[0][column]': '0',
'order[0][dir]': 'asc',
'start': '30',
'length': '10',
# 'search[value]':,
'search[regex]': 'false',
'_': '1607240121266'},
response = requests.get(url, data=json.dumps(Query_String_Parameters),headers=header)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)






