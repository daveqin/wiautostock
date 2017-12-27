# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:52:12 2017

@author: Administrator
"""

import math
import numpy as np
import pandas as pd
import tushare as ts
import h5py  #导入工具包
import matplotlib.pyplot as plt



#获取股票数据的api 
class stockapi:
    
    def __init__(self,stock ):
        self.stock     = stock
        self.hist_data = ts.get_hist_data(self.stock)
        
    #返回历史数据
    def get_hist(self):
        
        data1          =self.hist_data[['open','high','close','low']]
        
        return data1.to_json(orient='split')
    #返回成交量
    def get_nun(self):
        
        nun            = self.hist_data[['volume']]
        
        return nun.to_json(orient='split')
    #返回均线    
    def getMax(self,date):
        data=[]
        for i in  range(len(self.hist_data['close'])):
            
            data_ma    = [self.hist_data['close'][-(date-i):i+1]]
            #print np.mean(x60)
            data.append(np.mean(data_ma))
        return data
     #换手率   
     def get_turnover(self):
         data2       =self.hist_data[['turnover']]
         
         return data2
    #返回财务数据
    
    
        
#print data1.to_json(orient='split')


#st = stockapi("002486")
#print st.getMax(5)
#plt.plot(range(len(his_600848['ma20'])),his_600848['ma20'])

#print get_hist('002486')
#t=ts.get_report_data(2015,3)
#t.to_json('000875.json',orient='records')
#t.r
print pd.read_json('000875.json')
#f = h5py.File('test_s.h5','r')
#print f['data']

#a = np.random.standard_normal((900,4))
#b = pd.DataFrame(a)
#普通格式存储：
#h5 = pd.HDFStore('test_s.h5','w')
#h5['data'] = b
#h5.close()

