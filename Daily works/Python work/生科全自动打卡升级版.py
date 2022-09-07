from robobrowser import RoboBrowser
from time import sleep
headers = { 'User-Agent':'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}    
login_url = "https://xsc-health.wh.sdu.edu.cn/mobile/index.html#/common/office/fightncp/home"
rob = RoboBrowser(history=True,parser='lxml')
i=231
while i<=299:
	num="201900700"+str(i)
	password="whsdu@"+num
	rob.open(login_url,headers=headers)
	login_form = rob.get_form(class_name="login-form") 
	login_form["weui-cell cell username"].value = num
	login_form['password'].value = password
	rob.submit_form(login_form) 
	print(1)



