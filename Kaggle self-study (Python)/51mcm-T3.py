import pandas as pd
import numpy as np
import random
import math
import itertools
import heapq


def Taylor(t, n=50):
    # 计算前五十项
    sum_t = 0
    for i in range(n + 1):
        s = (-1) ** i * t ** (2 * i + 1) / (math.factorial(i) * 2 ** i * (2 * i + 1))
        sum_t += s
    return 0.5 + 1 / math.sqrt(2 * math.pi) * sum_t


def set_normalseed(data, data1, data2):
    for f in range(0, 4):
        for f_j in range(0, 10):
            # print(f_j,',',f)
            data.append(np.random.normal(data1[f_j, f], data2[f_j, f]))


#   均值
data1 = np.mat([[13.284036, 14.962134, 19.846022, 20.012922],
                [9.87088, 19.907534, 17.928158, 18.942358],
                [20.058414, 15.97263, 14.970352, 15.116388],
                [7.988652, 9.936646, 5.935868, 18.128398],
                [8.770062, 13.722012, 13.005208, 11.24949],
                [19.07412, 20.094358, 14.148532, 13.883878],
                [11.160148, 16.496146, 12.013664, 19.087604],
                [16.0201, 8.82748, 18.114384, 16.831394],
                [15.014602, 12.03512, 7.041914, 8.949654],
                [12.952448, 7.010982, 9.04917, 16.052406]])
# 标准差
data2 = np.mat([[1.262528917, 1.040711667, 1.089726857, 1.374675342],
                [0.912844245, 1.119335195, 0.949834207, 0.943654882],
                [0.919125009, 0.832702936, 1.019822179, 0.901205934],
                [0.96549009, 0.976417415, 0.19492674, 1.061939536],
                [0.863185422, 1.067506779, 0.911757145, 1.109426758],
                [1.155415745, 0.986646509, 0.935659811, 1.073187376],
                [1.013068014, 0.964085394, 0.886688065, 0.810161883],
                [1.063825743, 0.511280282, 1.034413526, 0.95538933],
                [0.986816797, 1.076138787, 0.365599114, 0.418563054],
                [0.455512308, 0.531209821, 0.455372472, 0.513219577]])
totallist = []
set_list = []
data = []
ls = []
probab = []
pp = 0
p = 0

data0 = np.mat([[13.284036, 14.962134, 19.846022, 20.012922],
                [9.87088, 19.907534, 17.928158, 18.942358],
                [20.058414, 15.97263, 14.970352, 15.116388],
                [7.988652, 9.936646, 5.935868, 18.128398],
                [8.770062, 13.722012, 13.005208, 11.24949],
                [19.07412, 20.094358, 14.148532, 13.883878],
                [11.160148, 16.496146, 12.013664, 19.087604],
                [16.0201, 8.82748, 18.114384, 16.831394],
                [15.014602, 12.03512, 7.041914, 8.949654],
                [12.952448, 7.010982, 9.04917, 16.052406]])
total = []
testlist = []




for qq in range(1, 11):
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
    total.append({"list&time": list, 'time': total_i}, )
    # print(total)
    p = p + 1
    print(p)

smallest_half = heapq.nsmallest(1088640, total, lambda x: x["time"])


totallist = []
for q in smallest_half:

    list = q['list&time']
    meet_con = []
    totallist.append(list)

    for mm in range(0, 25):
        p = []
        set_normalseed(p, data1, data2)

        data = p

        data0 = np.mat([data[:4],
                        data[4:8],
                        data[8:12],
                        data[12:16],
                        data[16:20],
                        data[20:24],
                        data[24:28],
                        data[28:32],
                        data[32:36],
                        data[36:40]])

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

        if (193.458394 - total_i) / 193.458394 >= 0.05:
            meet_con.append(data0[0, 0])
        else:
            continue
    # print('泰勒级数法计算结果：:[min,max]：', Taylor(3) - Taylor(-3))
    if meet_con:
        max_i = (max(meet_con) - data1[0, 0]) / data2[0, 0]
        min_i = (min(meet_con) - data1[0, 0]) / data2[0, 0]
        probab.append(Taylor(max_i) - Taylor(min_i))
        p_max = max(probab)
        file = open('E:\\pydata\\okokokok.txt', 'a', encoding='utf=8')
        data_ = str(p_max)
        data___ = str(list)
        file.write('最大概率：' + data_ + '\n' + '生产顺序：' + data___ + '\n')
        file.close()
    else:
        pass

    pp = pp + 1
    print(pp)

p_max = max(probab)
num = probab.index(max(probab))
print('最大概率：',p_max)
print('生产顺序：',totallist[num])
