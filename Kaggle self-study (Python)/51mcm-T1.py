import pandas as pd
import numpy as np
import random
import math
import itertools

data0 = np.mat([[13.284036,14.962134,19.846022,20.012922],
               [9.87088,19.907534,17.928158,18.942358],
                [20.058414,15.97263,14.970352,15.116388],
               [7.988652,9.936646,5.935868,18.128398],
                [8.770062,13.722012,13.005208,11.24949],
               [19.07412,20.094358,14.148532,13.883878],
               [11.160148,16.496146,12.013664,19.087604],
               [16.0201,8.82748,18.114384,16.831394],
                [15.014602,12.03512,7.041914,8.949654],
                [12.952448,7.010982,9.04917,16.052406]])
total = []
testlist = []
totallist = []
p = 0
set_list = []
ls = []

for qq in range(1,11):
    ls.append(qq)

for q in list(itertools.permutations(ls)):

    list = q
    meet_con = []
    totallist.append(list)

    t1 = data0[list[0] - 1, 0]  # 求T1,1

    t2 = 0  # 求max{T1,2, T2,1}
    if data0[list[0] - 1, 1] >= data0[list[1] - 1, 0]:
        t2 = data0[list[0] - 1, 1]
    elif data0[list[0] - 1, 1] < data0[list[1] - 1, 0]:
        t2 = data0[list[1] - 1, 0]

    tm = 0

    for m in range(3,len(list)):
        t3 = 0
        t4 = 0

        # 比大小MAX{T1,n,  T2,n-1,   T3,n-2,   T4,n-3}
        if data0[list[m - 3] - 1, 3] >= data0[list[m - 2] - 1, 2]:
            t3 = data0[list[m-3] - 1, 3]
        elif data0[list[m - 3] - 1, 3] < data0[list[m - 2] - 1, 2]:
            t3 = data0[list[m - 2] - 1, 2]
        if data0[list[m - 1] - 1, 1] >= data0[list[m] - 1, 0]:
            t4 = data0[list[m - 1] - 1, 1]
        elif data0[list[m - 1] - 1, 1] < data0[list[m] - 1, 0]:
            t4 = data0[list[m] - 1, 0]
        if t3 >= t4:
            tm = tm + t3
        elif t3 < t4:
            tm = tm + t4


    t5 = 0  # MAX{T1,3  , T2,2 ,  T3,1}
    if data0[list[0] - 1, 2] >= data0[list[1] - 1, 1]:
        t5 = data0[list[0] - 1, 2]
    elif data0[list[0] - 1, 2] < data0[list[1] - 1, 1]:
        t5 = data0[list[1] - 1, 1]
    if t5 >= data0[list[2] - 1, 0]:
        t5 = t5
    elif t5 < data0[list[2] - 1, 0]:
        t5 = data0[list[2] - 1, 0]

        # MAX{T2,10,  T3,9,  T4,8}
    t6 = 0

    if data0[list[9] - 1, 1] >= data0[list[8] - 1, 2]:
        t6 = data0[list[9] - 1, 1]
    elif data0[list[9] - 1, 1] < data0[list[8] - 1, 2]:
        t6 = data0[list[8] - 1, 2]
    if t6 >= data0[list[7] - 1, 3]:
        t6 = t6
    elif t6 < data0[list[7] - 1, 3]:
        t6 = data0[list[7] - 1, 3]



    # MAX{T3,10,  T4,9}
    t7 = 0
    if data0[list[9] - 1, 2] >= data0[list[8] - 1, 3]:
        t7 = data0[list[9] - 1, 2]
    elif data0[list[9] - 1, 2] < data0[list[8] - 1, 3]:
        t7 = data0[list[8] - 1, 3]

        # T4,10
    t8 = data0[list[9] - 1, 3]
    total_i = t1 + t2 + t5 + t6 + t7 + t8 + tm
    total.append(total_i)
    p = p+1
    print('=========', p, '==========')
print(len(totallist) - len(set_list), '次重复', '，', '占', (len(totallist) - len(set_list)) / len(totallist))
tmin = min(total)
num = total.index(min(total))
print('最小使用时间顺序：',totallist[num])
print('使用最短时间：',tmin,'s')
list = totallist[num]

timelist = []

t1 = data0[list[0] - 1, 0]  # 求T1,1

t2 = 0  # 求max{T1,2, T2,1}
if data0[list[0] - 1, 1] >= data0[list[1] - 1, 0]:
    t2 = data0[list[0] - 1, 1]
elif data0[list[0] - 1, 1] < data0[list[1] - 1, 0]:
    t2 = data0[list[1] - 1, 0]

tm = 0

for m in range(3, len(list)):
    t3 = 0
    t4 = 0

    # 比大小MAX{T1,n,  T2,n-1,   T3,n-2,   T4,n-3}
    if data0[list[m - 3] - 1, 3] >= data0[list[m - 2] - 1, 2]:
        t3 = data0[list[m - 3] - 1, 3]
    elif data0[list[m - 3] - 1, 3] < data0[list[m - 2] - 1, 2]:
        t3 = data0[list[m - 2] - 1, 2]
    if data0[list[m - 1] - 1, 1] >= data0[list[m] - 1, 0]:
        t4 = data0[list[m - 1] - 1, 1]
    elif data0[list[m - 1] - 1, 1] < data0[list[m] - 1, 0]:
        t4 = data0[list[m] - 1, 0]
    if t3 >= t4:
        tm = tm + t3
        timelist.append(t3)
    elif t3 < t4:
        tm = tm + t4
        timelist.append(t4)
print(timelist)
t5 = 0         # MAX{T1,3  , T2,2 ,  T3,1}
if data0[list[0] - 1, 2] >= data0[list[1] - 1, 1]:
    t5 = data0[list[0] - 1, 2]
elif data0[list[0] - 1, 2] < data0[list[1] - 1, 1]:
    t5 = data0[list[1] - 1, 1]
if t5 >= data0[list[2] - 1, 0]:
    t5 = t5
elif t5 < data0[list[2] - 1, 0]:
    t5 = data0[list[2] - 1, 0]

        # MAX{T2,10,  T3,9,  T4,8}
t6 = 0

if data0[list[9] - 1, 1] >= data0[list[8] - 1, 2]:
    t6 = data0[list[9] - 1, 1]
elif data0[list[9] - 1, 1] < data0[list[8] - 1, 2]:
    t6 = data0[list[8] - 1, 2]
if t6 >= data0[list[7] - 1, 3]:
    t6 = t6
elif t6 < data0[list[7] - 1, 3]:
    t6 = data0[list[7] - 1, 3]

    # MAX{T3,10,  T4,9}
t7 = 0
if data0[list[9] - 1, 2] >= data0[list[8] - 1, 3]:
    t7 = data0[list[9] - 1, 2]
elif data0[list[9] - 1, 2] < data0[list[8] - 1, 3]:
    t7 = data0[list[8] - 1, 3]

        # T4,10
t8 = data0[list[9] - 1, 3]
total_i = t1 + t2 + t5 + t6 + t7 + t8 + tm


t0_0 = 0
u = 0
t0_1 = t0_0 + t1
d0_1 = t1 + t2 + t5 + timelist[0]
d0_2 = d0_1 + timelist[1]
d0_3 = d0_2 + timelist[2]
d0_4 = d0_3 + timelist[3]
d0_5 = d0_4 + timelist[4]
d0_6 = d0_5 + timelist[5]
d0_7 = d0_6 + timelist[6]
d0_8 = d0_7 + t6
d0_9 = d0_8 + t7
d0_10 = d0_9 + t8
print('YM', list[0], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_1)
t0_0 = t0_1
t0_1 = t0_1 + t2
print('YM', list[1], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_2)
t0_0 = t0_1
t0_1 = t0_1 + t5
print('YM', list[2], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_3)
t0_0 = t0_1
t0_1 = t0_1 + timelist[0]
print('YM', list[3], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_4)
t0_0 = t0_1
t0_1 = t0_1 + timelist[1]
print('YM', list[4], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_5)
t0_0 = t0_1
t0_1 = t0_1 + timelist[2]
print('YM', list[5], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_6)
t0_0 = t0_1
t0_1 = t0_1 + timelist[3]
print('YM', list[6], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_7)
t0_0 = t0_1
t0_1 = t0_1 + timelist[4]
print('YM', list[7], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_8)
t0_0 = t0_1
t0_1 = t0_1 + timelist[5]
print('YM', list[8], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_9)
t0_0 = t0_1
t0_1 = t0_1 + timelist[6]
print('YM', list[9], '进入时刻', ':', '', t0_0, '；', '离开时刻', ':', d0_10)

