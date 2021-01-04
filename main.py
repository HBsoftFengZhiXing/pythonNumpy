# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import numpy as np
# ar = np.array([[1,2,3,4,5,6,9],[1,2,3,4,5,9,100],[1,2,3,4,5,9,100]])
# print(ar,type(ar))
# print(ar.ndim) #数组的维度
# print(ar.shape)
# print(ar.size)#数组中元素的个数
# print(ar.dtype)#数据的类型
# print(ar.itemsize)

# ary1 = np.array(range(10))
# ary2 = np.arange(10)
# ary3 = np.random.rand(10).reshape(2,5)
# ary4 = np.linspace(10,20,num = 21)

# a = np.array([1,  2,  3,4,5],dtype=complex)
# print (a)


# a = np.arange(24)
# print (a.ndim)             # a 现只有一个维度
# # 现在调整其大小
# b = a.reshape(2,4,3)  # b 现在拥有三个维度
# print(b)
# c= b.reshape(2,3,4)
# print(c)

#随机数
# a = np.random.normal(size=(4,4))#整他分布随机数
# b = np.random.rand(4)
# b = np.random.rand(2,4)
# print(a)
# print(b)
#
# data1 = np.random.rand(500)
# data2 = np.random.rand(500)
# import matplotlib.pyplot as plt
# plt.scatter(data1,data2)

import pandas as pd
import numpy as np

#ar = np.random.rand(3)*100
#print(ar)
#s = pd.Series(ar,index=list('acdef'),name='test')
#s = pd.Series(ar)
# print(s)
# print('------')
# print(type(s))
# print(s.index)
# print(s.values)
# print(s[:3])
# print(s[:-1])
# print(s['a':'c'])
# print('----------')
# print(bool(s.isnull))
# print(bool(s.notnull))
# print(s.head())#默认前五条
# print(s.tail())
# s1 = s.drop([2])
# print(s)
# print(s1)
# s2 = s.append(s1)
# print(s2)
# s2[0] = 100
# print(s2)

# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns=['Name','Age'],index=['a','b','c'])
# print(df)
#
# data1 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df1 = pd.DataFrame(data1)
# print(df1)
#
# data2 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df2 = pd.DataFrame(data2)
# print(df2)
#
# data3 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#       'two' : pd.Series([1, 2, 3,4], index=['a', 'b', 'c','d'])}
# df3 = pd.DataFrame(data3)
# print(df3)
#
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
#      'three' : pd.Series([10,20,30], index=['a','b','c'])}
#
# df = pd.DataFrame(d)
# print ("Our dataframe is:")
# print (df)
#
# # using del function
# print ("Deleting the first column using DEL function:")
# del df['one']
# print (df)
#
# # using pop function
# print ("Deleting another column using POP function:")
# df.pop('two')
# print (df)

df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns=['a','b','c','d'])
print(df1)
print(df1.sort_values(['a'],ascending=True))#排序，升序
print(df1.sort_values(['b'],ascending=False))

df2 = pd.DataFrame({'a':[1,1,1,1,2,2,2,2],'b':list(range(8)),'c':list(range(8,0,-1))})
print(df2)

import datetime
today1 = datetime.date.today()
print(today1,type(today1))

now = datetime.datetime.now()
print(now)

from dateutil.parser import  parse
date = '1/4/2021'
date2 = '2021/1/5'
print(parse(date),type(parse(date)))
print(parse(date2))

date3 = datetime.datetime.now() - parse((date))
print(date3)

date4 = datetime.datetime.now() + datetime.timedelta(days=1,hours=36)
print(date4)

d4 = pd.Timestamp.now()
print(d4,type(d4))

rng = pd.date_range('1/1/2012', periods=100, freq='H')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(rng)
print(len(rng))
print(ts)
print(len(ts))
t1 = pd.Timestamp(date)
print(t1)
print(pd.Timestamp(datetime.datetime.now()))

t2 = pd.to_datetime(date)
print(t2,type(t2))



