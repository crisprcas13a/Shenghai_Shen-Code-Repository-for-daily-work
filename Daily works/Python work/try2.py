import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])
# result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
# '缩略'
# arr = np.random.randn(4, 4)
# arr > 0
# np.where(arr > 0, 2, -2)
# y1 = np.array([-1,-2,-3,-4,-5,-6])
# y2 = np.array([1,2,3,4,5,6])
# y3 = np.zeros(6)
# cond = np.array([1,2,3,4,5,6])
# x = np.where(cond>5,y3,np.where(cond>2,y1,y2))
# print (x) # [ 1.  2. -3. -4. -5.  0.]
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:   
#         return (n*factorial(n-1))

# a = factorial(5)
# print(a)
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002, 2003],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data) 
# print(frame['year']
# df = pd.DataFrame([['乔峰', '男', 95, '降龙十八掌', '主角'],
#         ['虚竹', '男', 93, '天上六阳掌', '主角'],
#         ['段誉', '男', 92, '六脉神剑', '主角'],
#         ['王语嫣', '女', 95,'熟知武诀', '主角'],
#         ['包不同', '男', 65, '胡搅蛮缠', '配角'],
#         ['康敏', '女', 40, '惑夫妒人', '配角']],
#         index=list('abcdef'.upper()), n 
#         columns=['name', 'gender', 'score', 'skill', 'class'])
# print(df.iat[1])
# obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
# print(obj.rank( method='min'))
# names = ['a', 'b', 'c', 'd', 'message']
# df=pd.read_csv('C:\\Users\\Zz\\Desktop\\pydata-book-2nd-edition\\examples\\ex1.csv',names=names,index_col='message')
# print(df)
# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
# cats = pd.cut(ages, bins)
# print(cats )
# df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
# sampler = np.random.permutation(5)
# print(sampler)
# frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
#                     'c': ['one', 'one', 'one', 'two', 'two',
#                             'two', 'two'],
#                     'd': [0, 1, 2, 0, 1, 2, 3]})
# print()
# df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                     'data1': range(7)})
# df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
#                     'data2': range(3)})
# print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
# data1 = pd.DataFrame(
# np.arange(0,16).reshape(4,4),
# columns=list('abcd')
# )
# data1
# data2 = [
#   [4,1,5,7],
#   [6,5,7,1],
#   [9,9,123,129],
#   [16,16,32,1]
# ]
# data1.columns = list('abcd')
# data2.columns =list('abcd')
# data3 = data2
# print(pd.concat([data1,data2,data3],keys=['data1','data2','data3'])) 
# data = pd.DataFrame(np.arange(6).reshape((2, 3)),
#                     index=pd.Index(['Ohio', 'Colorado'], name='state'),
#                     columns=pd.Index(['one', 'two', 'three'],
#                     name='number'))
# print(data.unstack(0))    
# data = np.arange(10)
# plt.plot(data)
# fig = plt.figure()
# ax3 = fig.add_subplot(2, 2, 3)
# # ax3.show()
# plt.show()
#8080ff
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# _ = ax1.hist(np.random.randn(100), bins=20, color='#8080ff', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
# plt.show()
# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(np.random.randn(500), bins=50, color='darksalmon', alpha=0.5)
# plt.subplots_adjust(wspace=0, hspace=0)
# plt.show()
# plt.figure()
# plt.plot(np.random.randn(30), 'ko--')
# plt.show()
# data = np.random.randn(30).cumsum()
# plt.plot(data, 'k--', label='Default')
# plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
# plt.legend(loc='best')
# plt.show()
# from numpy.random import randn
# fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
# ax.plot(randn(1000).cumsum(), 'b', label='one')
# ax.plot(randn(1000).cumsum(), 'k--', label='two')
# ax.plot(randn(1000).cumsum(), '#00ffff', label='three')
# props={'title':'lines','xlabel':'stages'}
# ax.set(**props)
# ax.legend(loc='best')
# plt.show()
# fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
# a=data.index
# b=data
# def job(a,b,props):
#     a.legend(loc='best'),b.legend(loc='best')
#     b.set(**props)
# data.plot(kind='bar', ax=axes[0], color='salmon', alpha=0.7,label='kinds')
# data.plot(kind='barh', ax=axes[1], color='#ff80ff', alpha=0.7,label='kinds')
# for x,y in zip(a,b):
#     axes[0].text(x,y+0.03,'%.5f' % y,fontdict={'fontsize':10},verticalalignment='center',\
#         horizontalalignment='center')
# props={'xlabel':'BookID','title':'Counter'}
# job(axes[0],axes[1],props)
# plt.show()
# np1=np.arange(12).reshape((3,4))
# df=pd.DataFrame(np1,index=['a','b','c'],columns=[1,2,3,4])
# sns.barplot(x=df[3],y=df[2],data=df,orient='h')
# plt.show()
# tips = pd.read_csv('C:\\Users\\Zz\\Desktop\\pydata-book-2nd-edition\\examples\\tips.csv')
# tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
# tips.head()
# tips['tip_pct'].plot.hist(bins=50)
# sns.set(style="whitegrid")
# plt.show()
# comp1 = np.random.normal(0, 1, size=200)
# comp2 = np.random.normal(10, 2, size=200)
# values = pd.Series(np.concatenate([comp1, comp2]))
# sns.distplot(values, bins=100, color='k')
# macro = pd.read_csv('C:\\Users\\Zz\\Desktop\\pydata-book-2nd-edition\\examples\\macrodata.csv')
# data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
# trans_data = np.log(data).diff().dropna()
# trans_data[-5:]
# sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
# sns.regplot('m1', 'unemp', data=trans_data,color='#8080ff')
# plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))
# tips = sns.load_dataset("tips")
# ax = sns.scatterplot(x="total_bill", y="tip", data=tips)
# df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
#                 'key2' : ['one', 'two', 'one', 'two', 'one'],
#                 'data1' : np.random.randn(5),
#                 'data2' : np.random.randn(5)})
# pieces = dict(list(df.groupby('key1')))
# print(pieces)
# print(type(df.groupby(['key1', 'key2'])['data2'].mean()))
# fruits = ['apple', 'orange', 'apple', 'apple'] * 2
# N = len(fruits)
# df = pd.DataFrame({'fruit': fruits,
#                 'basket_id': np.arange(N),
#                 'count': np.random.randint(3, 15, size=N),
#                 'weight': np.random.uniform(0, 4, size=N)},
#                 columns=['basket_id', 'fruit', 'count', 'weight'])
# fruit_cat = df['fruit'].astype('category')
# print(fruit_cat)
# np.random.seed(12345)
# draws = np.random.randn(1000)
# bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
# bins = pd.Series(bins, name='quartile')
# results = (pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']))
# print(results)
# import statsmodels.api as sm
# import statsmodels.formula.api as smf
# def dnorm(mean, variance, size=1):
#     if isinstance(size, int):
#         size = size,
#     return mean + np.sqrt(variance) * np.random.randn(*size)
# N = 100
# X = np.c_[dnorm(0, 0.4, size=N),
#         dnorm(0, 0.6, size=N),
#         dnorm(0, 0.2, size=N)]
# eps = dnorm(0, 0.1, size=N)
# beta = [0.1, 0.3, 0.5]
# df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
#                     'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
# df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
#                     'hire_date': [2004, 2008, 2012, 2014]})
# # df3 = pd.merge(df1, df2)
# # print(df3) 
# df1a = df1.set_index('employee')
# df2a = df2.set_index('employee')
# print(pd.merge(df1a, df2a, left_index=True, right_index=True))
# df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
#                     'rank': [1, 2, 3, 4]})
# df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
#                     'rank': [3, 1, 4, 2]})
# print(pd.merge(df8, df9, on="name"))
import random

# i=1
# q=0
# while i <=1000000:
#     a=random.randint(0,6)
#     b=random.randint(0,6)
#     c=random.randint(0,6)
#     n=0
#     n=a+b+c
#     if n==6:
#         q+=1
#     i+=1

# print(q)
n=1
while n<3:
    b=random.randint(0,6)
    print(b)
    n+=1


































































































































