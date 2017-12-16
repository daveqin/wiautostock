# -*- coding: gb2312 -*-
"""
Created on Mon Nov 20 10:55:56 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
import time
import pandas as pd
#return date Mean  data
def getMax(date,his_stock):
    x=[]
    for i in  range(len(his_stock['close'])):
        
        x60 = [his_stock['close'][-(date-i):i+1]]
        #print np.mean(x60)
        x.append(np.mean(x60))
    return x
def getMix(date,his):
    Mix = []
    for i in  range(len(his['close'])):
        Mix.append(np.max(his['close'][-(date-i):i+1]))
    return Mix

def getMin(date,his):
    Min = []
    for i in  range(len(his['close'])):
        Min.append(np.min(his['close'][-(date-i):i+1]))
    return Min
#if (ma5 > ma30) & (ma10 > ma30) & (ma60<ma30) buy else sell

def getNew(stock):
    df1=ts.get_realtime_quotes('002486')#
    nowTime = [time.strftime('%Y-%m-%d',time.localtime(time.time()))]  #get time
    dd = round(float(df1['price'][0]),2)
    
    datV =[["22","22",dd,"22","22","22","22","22","22","22","22","22","22","22"]] 
    dat = ["open","high","close","low","volume","price_change","p_change","ma5","ma10","ma20","v_ma5","v_ma10","v_ma20","turnover"]
    df = pd.DataFrame(datV,index=nowTime,columns=dat) 
    return df
    
def stock_ma60(stock):
    stock = stock
    nowTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))  #get time
    his_stock=ts.get_hist_data(stock,start='2017-011-01',end=nowTime) #get a stock histor
    his_stock = his_stock.sort_index()
    his_stock=pd.concat([his_stock,getNew(stock)],axis=0)#
    close = his_stock['close']
    MA5 = getMax(5,his_stock)
    MA10 = getMax(10,his_stock)
    MA30 = getMax(30,his_stock)
    MA60 = getMax(60,his_stock)
    
    c=np.array(close)
    a5=np.array(MA5)
    a10=np.array(MA10)
    a30=np.array(MA30)
    a60=np.array(MA60)
    MA5_c = a5-c
    MA5_10 = (a5-a10)
    MA5_60 =  (a5-a60)/c
    MA10_30=  (a10-a30)
    MA30_60 = (a30-a60)
    
    
    
    if(MA30_60[-1] > 0):
        if(MA10_30[-1]>0):
            if(MA5_60[-1]>0.15):
                if(MA5_c[-1]<0):
                    return 'nobuy'
                return  'buy'
            else:
                if(MA5_10[-1]>0):    
                    return  'buy'
                else:
                    return 'nobuy'
        else:
            return  'nobuy'
    else:
        return  'nobuy'


res = stock_ma60('600887')  
print res      
