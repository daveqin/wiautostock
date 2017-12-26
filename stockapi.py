# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:52:12 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
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
            
            data_ma       = [self.hist_data['close'][-(date-i):i+1]]
            #print np.mean(x60)
            data.append(np.mean(data_ma))
        return data
        
        
    #返回财务数据
    
    
        
#print data1.to_json(orient='split')


st = stockapi("002486")
print st.getMax(5)
plt.plot(range(len(his_600848['ma20'])),his_600848['ma20'])

#print get_hist('002486')

