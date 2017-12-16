# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:31:19 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt


x = 2000
y = 5.5*100

e = x/y

print int(e)

his_600848=ts.get_hist_data('601318',start='2017-06-01',end='2017-11-16') #get a stock histor

#print his_600848['open']
#print his_600848['close']
his_600848['changfo']=((his_600848['close']-his_600848['open'])/his_600848['close'])*100 #计算涨幅并且增加数据到panda组里面去

his_600848['pre_close'] =[his_600848['close'][i-1] for i in range(len(his_600848['close'])) ]

his_600848 = his_600848.sort_index()    #sort index min to max



plt.plot(range(len(his_600848['close'])),his_600848['close'],color='black')
plt.plot(range(len(his_600848['ma5'])),his_600848['ma5'])
plt.plot(range(len(his_600848['ma10'])),his_600848['ma10'])
plt.plot(range(len(his_600848['ma20'])),his_600848['ma20'])

#return date Mean  data
def getMax(date,his_600848):
    x=[]
    for i in  range(len(his_600848['close'])):
        
        x60 = [his_600848['close'][-(date-i):i+1]]
        #print np.mean(x60)
        x.append(np.mean(x60))
    return x

x = getMax(30,his_600848)

plt.plot(range(len(x)),x)
