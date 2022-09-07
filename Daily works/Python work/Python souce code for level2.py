'''Made by Farmmer.Shen
值作为交流讨论，请勿用作其它用途'''

'华氏度摄氏度转换'
# Temp=input('请输入带有符号的温度:')
# if Temp[-1] in ['F','f']:
#     C=(eval(Temp[0:1])-31)/1.8
#     print("转换后的温度为{;.2f}C:".format(C))
# elif Temp[-1] in ['C','C']:
#     F=1.8*eval(Temp[0:-1])+32
#     print("转换后的温度为{;.2f}F:".format(F))
# else:
#     print("错了啦")

'画出python蟒蛇'
# import turtle
# turtle.setup(658,350,200,208)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize (25)
# turtle.pencolor ("purple")
# turtle.seth(-40)
# for i in range (4):
#     turtle. circle(40, 80)
#     turtle.circle(-40, 80)
#     turtle. circle(40, 80/2)
#     turtle.fd(40)
#     turtle. circle(16, 180)
#     turtle.fd(40* 2/3)
#     turtle. done()

'天天向上'
# dayfactor =0.005
# dayup = pow(1+dayfactor, 365)
# daydown= pow(1-dayfactor, 365)
# print("向上:{:,2f}向下:{:2f}", format( dayup, daydown)

'天天向上2'
# def dayUp(df):
#     dayup =1
#     for i in range(365):
#         if i%7in[6,8]:
#             dayup= dayup*(1-0.01)
#         else:
#             dayup=dayup*(1+ df)
#     return dayup
# dayfactor = 0.01
# while dayUp (dayfactor)< 37.78:
#     dayfactor += 0.001
# print("努力参数为：{:.3f}".format(dayfactor))

'获取星期'
# weekstr="ー二三四五六日"
# weekid=eval( input("请输入星期数字（1-7):"))
# print("星期"+ weekstr[ weekid-1])

'打印星座'
# for i in range(12):
#     print(chr(9800+i),end="")

# print("{0:=^20}".format("python"))
# print("{:b}".format(123))

'获取时间'
# import time as tt
# print(tt.ctime())
# t =tt.gmtime()
# print(tt.strftime("%Y-%m-%d %H:%M:%S",t))

'文本进度条'
# import time
# scale=50
# print("执行开始".center(scale//2,'-'))
# start=time.perf_counter()
# for i in range(scale+1):
#     a='*'*i
#     b='.'*(scale-i)
#     c =(i/scale)*100
#     dur=time.perf_counter()-start
#     print(" \r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b,dur),end='')
#     time.sleep(0.1)
# print("结束".center(scale//2,'-'))

'BMI指数'
# height, weight=eval( input("请输入身高（米）和体重（公斤）【逗号隔开】:"))
# bmi =weight/ pow(height, 2)
# print("BMI数值为：{：2f}".format(bmi))
# who=""
# if bmi<18.5:
#     who="偏瘦"
# elif 18.5<=bmi<25:
#     who="正常"
# elif 25 <=bmi<30:
#     who="偏胖"
# else:
#     who="肥胖"
# print("BMI指标为：国际'{}", format(who))

'圆周率计算'
# from random import random
# from time import perf_counter
# DARTS=1000*1000
# hits =0.0
# start =perf_counter ()
# for i in range(1, DARTS+1):
#     x, y=random(), random()
#     dist =pow(x ** 2+y **2, 0.5)
#     if dist < 1.0:
#         hits = hits +1
# pi =4 *(hits/DARTS)
# print(pi)

'时间绘图二极管'
# import turtle
# import  time
# def drawline(draw):
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     turtle.right(90)
# def drawdigit( digit):
#     drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
#     drawline (True) if digit in [0, 2,3,5, 6,8,9] else drawline(False)
#     drawline(True)if digit in [0, 2, 6, 8] else drawline(False)
#     turtle.left(90)
#     drawline (True)if digit in [0, 4, 5, 6,8,9] else drawline(False)
#     drawline(True) if digit in [0, 2, 3, 5, 6,7,8,9] else drawline(False)
#     drawline(True) if digit in [0, 1, 2, 3, 4, 7,8,9] else drawline(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
# def drawdate(date):
#     turtle. pencolor("red")
#     for i in date:
#         if i=='-':
#             turtle.write("年",font=("Arial", 18, "normal"))
#             turtle.pencolor("green")
#             turtle.fd(40)
#         elif i =="=":
#             turtle.write("月", font=("Arial", 18, "normal"))
#             turtle. pencolor("blue")
#             turtle.fd(40)
#         elif i=="+":
#             turtle.write("日",font=("Arial", 18, "normal"))
#         else:
#             drawdigit(eval(i))
# def main():
#     turtle.setup(80,350,20,20)
#     turtle.penup ()
#     turtle.fd(-300)
#     turtle.pensize(5)
#     drawdate( time.strftime('%Y-%m=%d+',time.gmtime()))
#     turtle.hideturtle()
#     turtle. done()
# main()

'反转'
# def rvs(s):
#     if s=="":
#         return(s)
#     else:
#         return(rvs(s[1:])+s[0])
# print(rvs('youtube'))

'汉诺塔问题'
# count =0
# def hanoi(n, src, dst, mid):
#     global count
#     if n==1:
#         print("{}:{}->{}".format(1, src, dst))
#         count + 1
#     else:
#         hanoi(n-1, src, mid, dst)
#         print("{}:{}->{}".format(n, src, dst))
#         count + 1
#         hanoi(n-1, mid, dst, src)
# hanoi(30,'First','Second','Third')

'科赫雪花'
# import turtle
# def koch(size, n):
#     if n==0:
#         turtle.fd(size)
#     else:
#         for angle in [0,60,-120,60]:
#             turtle.left(angle)
#             koch(size/3, n-1)
# def main():
#     turtle.setup(600,600)
#     turtle.penup()
#     turtle.goto(-200,100)
#     turtle.pendown()
#     turtle.pensize(2)
#     level = 3
#     koch(400,level)
#     turtle.right(120)
#     koch(400,level)
#     turtle.right(120)
#     koch(400,level)
#     turtle.hideturtle()
#     turtle.done()
# main()

'基础数据分析'
# def getnum():
#     nums = []
#     inumstr= input("请输入数字（回车退出）：")
#     while inumstr !="":
#         nums. append(eval( inumstr))
#         inumstr= input("请输入数字（回车退出）：")
#     return nums

# def mean(numbers):
#     s=0.0
#     for num in numbers:
#         s=s+num
#     return s/len(numbers)

# def dev(numbers,mean):
#     sdev=0.0
#     for num in numbers:
#         sdev=sdev+(num-mean)**2
#     return pow(sdev/(len(numbers)-1),0.5)

# def median(numbers):
#     sorted(numbers)
#     size= len(numbers)
#     if size%2==0:
#         med =(numbers[size//2-1]+numbers[size//2])/2
#     else:
#         med =numbers[size//21]
#     return med

'Hamlet词频统计'
# def gettext():
#     txt=open("hamlet.txt","r").read()
#     txt =txt.lower()
#     for ch in'!$%&()@#/?<>+=.,^*':
#         txt=txt.replace(ch, "")
#     return txt
# hamlettext=gettext()
# words=hamlettext.split()
# counts={}
# for word in words:
#     counts[word]=counts.get(word,0)+1 #相当于新增了一个字典元素
# items =list(counts.items())
# items.sort(key=lambda x:x[1],reverse=True)#按第二个元素排列
# for i in range(10):
#     word,counts=items[i]
#     print("{0:<10}{1:>5}".format(word,counts))

'三国演义词频统计'
# import jieba
# txt = open("threekingdoms.txt","r" , encoding="utf-8").read ()
# excludes={"将军","却说","荆州","二人","不可","不能","如此"}
# words =jieba. lcut(txt)
# counts ={}
# for word in words:
#     if len(word)==1:
#         continue
#     else:
#         counts[word]=counts.get(word,0)+1 #相当于新增了一个字典元素
# items =list(counts.items())
# items.sort(key=lambda x:x[1],reverse=True)#按第二个元素排列
# for i in range(15):
#     word,counts=items[i]
#     print("{0:<10}{1:>5}".format(word,counts))

'轨迹自动绘制'
# import turtle as t
# t. title('自动轨迹绘制')
# t.setup(880,600,0)
# t .pencolor("red")
# t .pensize(5)
# datals=[]
# f=open("data.txt")
# for line in f:
#     line =line.replace("\n", "")
#     datals.append(list(map(eval, line.split(","))))#map将第一个的功能作用于第二个参数的每一个对象
# f.close()
# for i in range(len(datals)):
#     t .pencolor(datals[i][3], datals[i][4], datals[i][5])
#     t .fd(datals[i][0])
#     if datals[i][1]:
#         t .right(datals[i][2])
#     else:
#         t .left(datals[i][2])

'第三方库自动安装脚本'
# import os
# libs={'numpy', 'matplotlib','pillow','sklearn','requests',\
# 'jieba', 'beautifulsoup4', 'wheel', 'networkx', 'sympy',\
# 'pyinstaller', 'django,flask', 'werobot', 'pyqt5' ,\
# 'pandas', 'pyopengl', 'pypdf2', 'docopt', 'pygame'}
# try:
#     for lib in libs:
#         os.system("pip install "+lib)
#         print("successful")
# except:
#     print("Failed Somehow")











