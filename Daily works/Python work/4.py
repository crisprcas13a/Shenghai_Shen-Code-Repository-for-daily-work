from __future__ import division
list1=[2.59,5.59,9.00,11.58,14.58,17.58,20.57,23.57,26.59,30.00,35.00,40.01,45.01,50.03]
# for number  in list1:
# 	(float(number)-int(number))/60+int(number)
list3=[(float(number)-int(number))/0.6+int(number) for number  in list1]
# list4=[float("%4f"%x for x in list3)]
# c = ['{:.4f}'.format(i) for i in list3] 
print(c)
