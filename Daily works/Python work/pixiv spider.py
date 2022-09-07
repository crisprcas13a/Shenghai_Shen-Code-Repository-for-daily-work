import requests
from fake_useragent import UserAgent
import json
import re
import os

global i
i = 0
ua = UserAgent()  # 生成假的浏览器请求头,防止被封ip
user_agent = ua.random  # 随机选择一个浏览器
proxies = {'http': 'http://127.0.0.1:51837', 'https': 'http://127.0.0.1:51837'} # 代理,根据自己实际情况调整,注意在请求时一定不要忘记代理!!


def makefolder(id): # 根据画师的id创建对应的文件夹
	try:
		folder = os.path.join('E:\pixivimages', id)
		os.mkdir(folder)
		return folder
	except(FileExistsError):
		print('the folder exists!')
		exit()


def getAuthorAllPicID(id, cookie): # 获取画师所有图片的id
	url = 'https://pixiv.net/ajax/user/' + id + '/profile/all' # 访问存有画师所有作品
	headers = {
		'User-Agent': user_agent,
		'Cookie': cookie,
		'Referer': 'https://www.pixiv.net/artworks/' 
	}
	res = requests.get(url, headers=headers, proxies=proxies)
	if res.status_code == 200:
		resdict = json.loads(res.content)['body']['illusts']  # 将json转化为python的字典后提取元素
		return [key for key in resdict]  # 返回所有图片id
	else:
		print("Can not get the author's picture ids!")
		exit()


def getPictures(folder, IDlist, cookie): # 访问图片储存的真实网址
	for picid in IDlist:
		url1 = 'https://www.pixiv.net/artworks/{}'.format(picid)  # 注意这里referer必不可少,否则会报403
		headers = {
			'User-Agent': user_agent,
			'Cookie': cookie,
			'Referer': url1
		}
		url = 'https://www.pixiv.net/ajax/illust/' + str(picid) + '?lang = zh' #访问储存图片网址的json
		res = requests.get(url, headers=headers, proxies=proxies)
		if res.status_code == 200:
			data = json.loads(res.content)
			picurl = data['body']['urls']['original'] # 在字典中找到储存图片的路径与标题
			title = data['body']['title']
			title = changeTitle(title) # 调整标题
			print(title)
			print(picurl)
			download(folder, picurl, title, headers)
		else:
			print("Can not get the urls of the pictures!")
			exit()


def changeTitle(title): # 为了防止
	global i
	title = re.sub('[*:]', "", title) # 如果图片中有下列符号,可能会导致图片无法成功下载
	# 注意可能还会有许多不能用于文件命名的符号,如果找到对应符号要将其添加到正则表达式中
	if title == '無題': # pixiv中有许多名为'無題'(日文)的图片,需要对它们加以区分以防止覆盖
		title = title + str(i)
		i = i + 1
	return title


def download(folder, picurl, title, headers): # 将图片下载到文件夹中
	img = requests.get(picurl, headers=headers, proxies=proxies)
	if img.status_code == 200:
		with open(folder + '\\' + title + '.jpg', 'wb') as file:  # 保存图片
			print("downloading:" + title)
			file.write(img.content)
	else:
		print("download pictures error!")


def main():
	global i
	id = input('input the id of the artist:')
	cookie = input('input your cookie:') # 半自动爬虫,需要自己事先登录pixiv以获取cookie
	folder = makefolder(id)
	IDlist = getAuthorAllPicID(id, cookie)
	getPictures(folder, IDlist, cookie)


if __name__ == '__main__':
	main()

