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
import json 



#获取股票数据的api 
class stockapi:
    
    def __init__(self,stock ):
        self.stock     = stock
        self.hist_data = ts.get_hist_data(self.stock,start='2017-01-01')
        self.hist_data = self.hist_data.sort_index()
        
    #返回历史数据
    def get_hist(self):
        
        data1          =self.hist_data[['open','close','high','close']]
        
        return data1.to_json(orient='split')
    #返回成交量
    def get_nun(self):
        
        nun      = self.hist_data[['volume']]
        nun      = nun.T
        return nun.to_json(orient='split')
    #返回均线    
    def getMax(self,date):
        data=[]
        for i in  range(len(self.hist_data['close'])):
            
            data_ma    = [self.hist_data['close'][-(date-i):i+1]]
            #print np.mean(x60)
            data.append(np.mean(data_ma))
        return data
    #获取收盘价
    def get_clos(self):
         
        data1      =self.hist_data[['close']]
        data1      = data1.T
       
        return data1.to_json(orient='split')
       
    #涨跌幅
    def get_change(self):
         data2       =self.hist_data[['p_change']]
         data2      = data2.T
         return data2.to_json(orient='split')
    #换手率   
    def get_turnover(self):
         data2       =self.hist_data[['turnover']]
         
         return data2.to_json(orient='split')
    #返回财务数据
    
    
    #获取行情数据
    def get_all(self):
        
        #data = ts.get_today_all()
        #data = data[['code','name','changepercent']]
        data = pd.read_json('2017_12_30.json')
      
        return data.to_json(orient='split')
    
    
    
#t = stockapi('000002')
#print t.get_all()        
#print data1.to_json(orient='split')



#print st.getMax(5)
#plt.plot(range(len(his_600848['ma20'])),his_600848['ma20'])

#print get_hist('002486')
#t=ts.get_report_data(2015,3)
#t.to_json('000875.json',orient='records')
#t.r
#print pd.read_json('000875.json')
#f = h5py.File('test_s.h5','r')
#print f['data']

#a = np.random.standard_normal((900,4))
#b = pd.DataFrame(a)
#普通格式存储：
#h5 = pd.HDFStore('test_s.h5','w')
#h5['data'] = b
#h5.close()

