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
import talib
import datetime
import os



#获取股票数据的api 
class stockapi:
    
    def __init__(self,stock ):
        self.stock     = stock
        self.hist_data = ts.get_hist_data(self.stock,start='2017-01-01')
        self.hist_data = self.hist_data.sort_index()
       
    #返回历史数据
    def get_hist(self):
        
        data1=self.hist_data[['open','close','high','close']]
        
        return data1.to_json(orient='split')
    #获取k线图与历史数据
    def get_hist_k(self):
        
        data1      =self.hist_data[['open','close','high','close']]
        inde       =list(data1.index)
        datav      =data1.values
        ma60       =list(np.nan_to_num(self.getMax(60)))
        data       ={'index':inde,'data':datav.tolist(),'ma60':ma60}
        
        return json.dumps(data)
        #print json.dumps(data)
        
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
     
    #返回净利润
    def get_net_profits(self):
        
        data     = pd.read_json('profit_data/20170103.json')
        data     = data[data.code==int(self.stock)]
        profitss =data['net_profits'].values
        dates    =data['date'].values
        
        data = {'profitss':profitss.tolist(),'dates':dates.tolist()}
        
        return json.dumps(data)
    
    
    #获取行情数据
    def get_all(self):
        now      = datetime.datetime.now()
        n        = now.strftime('%Y-%m-%d')
        filename = 'nowdata/'+str(n)+'.json'
        print(filename)
        if(os.path.exists(filename)):
            data = pd.read_json(filename)
            data = data[['code','name','changepercent']]
           
        else:
            data  = ts.get_today_all()
            data.to_json(filename,orient='records')
            
       
        
      
        return data.to_json(orient='split')
    
    
    
#t = stockapi('600550')
#print(t.get_all())

#盈利能力
def all_proft():
    year = [2014,2015,2016,2017]
    m    = [1,2,3,4]
    for y in year:
        for n in m:
            print (str(y)+str(n))
            data = ts.get_profit_data(y,n)
            data['date'] = str(y)+str(n)
            data.to_json('profit_data/'+str(y)+str(n)+'.json',orient='records')
            
        
    
    
    #data = pd.concat([data1,data2],axis=0)
    
    return data
    
def to():
    year = [2015,2016,2017]
    m    = [1,2,3,4]
    data1 = pd.read_json('profit_data/20141.json')
    data2 = pd.read_json('profit_data/20142.json')
    data3 = pd.read_json('profit_data/20143.json')
    data4 = pd.read_json('profit_data/20144.json')
    
    data1=pd.concat([data1,data2],axis=0)
    data1=pd.concat([data1,data3],axis=0)
    data1=pd.concat([data1,data4],axis=0)
    
    for y in year:
        for n in m:
            if (str(y)!='2017')&(str(m)!='4'):
                data0 =pd.read_json('profit_data/'+str(y)+str(n)+'.json')
                data1=pd.concat([data1,data0],axis=0)
    data1.to_json('profit_data/20170103.json',orient='records')        
    print (data1)
    

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

